import os
import re
from unstructured.partition.pdf import partition_pdf
from unstructured_pytesseract import pytesseract
from nltk.corpus import stopwords
import nltk
from typing import List, Optional
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from typing import Optional

# Certifique-se de que os recursos do NLTK estão baixados 
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    print("Baixando recursos do NLTK (stopwords)...")
    nltk.download('stopwords')

# Carrega o modelo de português do spaCy, um modelo de linguagem pré treinado
try:
    nlp = spacy.load("pt_core_news_sm")
except OSError:
    print("Aviso: O modelo 'pt_core_news_sm' não foi encontrado.")
    print("Execute 'python -m spacy download pt_core_news_sm' para baixar o modelo.")
    # Define nlp como None para evitar erros se o modelo não puder ser carregado
    nlp = None
 
# Inserir o caminho do 'tesseract.exe' na sua máquina.
TESSERACT_PATH = r'CAMINHO DO tesseract.exe' #<-------------------------------------------------------------------------------------

# Define o caminho do Tesseract para o unstructured_pytesseract
if os.path.exists(TESSERACT_PATH):
    pytesseract.tesseract_cmd = TESSERACT_PATH
else:
    print(f"ERRO: Tesseract não encontrado em {TESSERACT_PATH}. O OCR pode não funcionar.")

# Define as stopwords em português, usamos lista pré existente da nltk.corpus.
STOPWORDS_PT = set(stopwords.words('portuguese')) 

#---------------------------------------------------------------------------------------------------------------------#

def extrair_texto_completo_do_pdf(pdf_path: str) -> str: #Lê o PDF, extrai todo o texto e retorna uma string.
   
    print(f"Iniciando extração de texto de: {pdf_path}")
    
    try:
        # Extrai o documento usando o OCR.
        elementos = partition_pdf(
            filename=pdf_path,
            ocr_strategy="hi_res"
        )
    except Exception as e:
        return f"Erro ao particionar o PDF: {e}"
    
    # Junta todos os elementos em uma única string de texto
    texto_completo = "\n\n".join(str(elemento) for elemento in elementos)
    
    if not texto_completo:
        return "Não foi possível extrair texto do PDF."
    
    return texto_completo

#---------------------------------------------------------------------------------------------------------------------#

def remover_stopwords(texto: str, stopwords_set: set) -> list:
    
    #Converte todas as letras para minúscula e remove pontuação e caracteres especiais
    texto = re.sub(r'[^\w\s]', '', texto.lower())
    
    #Tokeniza (divide em palavras)
    palavras = texto.split()
    
    #Filtra as stopwords percorrendo cada uma das palavras e vendo se elas estão contidas na lista de stopwords ou não.
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords_set]
    
    return palavras_filtradas

#---------------------------------------------------------------------------------------------------------------------#

def calcular_frequencia_top_n(vetor_palavras: list, n: int = 10) -> list: 
    # vetor_palavras é uma lista de palavras tokenizadas
    # n é a quantidade de palavras mais frequêntes que devem ser retornadas
    
    frequencias = {} # Usando um dicionário para armazenar as frequências
    for palavra in vetor_palavras:
        # Aumenta a contagem da palavra se ela já existe. Se a palavra for nova, inicializa com 1.
        frequencias[palavra] = frequencias.get(palavra, 0) + 1
    
    # ordena os intens do dicionario usando sorted().
    itens_ordenados = sorted(
        frequencias.items(), # items() retorna uma lista de tuplas (chave, valor) onde chave é a palavra e valor sua frequência.
        key=lambda item: item[1], 
        reverse=True # garante a ordem decrescente.
    )
    
    return itens_ordenados[:n] #retorna os N primeiros elementos da lista ordenada

#---------------------------------------------------------------------------------------------------------------------#

def extrair_referencias_do_texto(texto_completo: str) -> str:

    referencias = ""
    
    # Busca pelo título da seção (Referências, Bibliografia, etc.) o padrão r'^\s*' permite espaços antes do título. 
    # O r'[\s\n]*$' permite espaços/quebras depois.
    titulos_referencias = r'^\s*(refer[êe]ncias|bibliografia|refer[êe]ncias bibliogr[áa]ficas)[\s\n]*$'
    
    # Procura pelo título no texto que corresponde as referências
    match_end = re.search(titulos_referencias, texto_completo, re.IGNORECASE | re.MULTILINE) 
    # re.IGNORECASE garante que a busca não sera sencivel a maiusculas e minisculas
    # re.MULTILINE: Faz com que '^' e '$' correspondam ao início/fim de cada, e não apenas do texto.
    # re.search metodo usado para buscar padrão em strings, retorna o primeiro correspondente encontrado.

    if match_end:
        # Pega o texto a partir do ponto onde o título termina, ignorando espaços/quebras
        start_index = match_end.end()
        referencias = texto_completo[start_index:].strip()
        
        # Para leitura do texto ao encontrar algum desses marcadores que costumam vir apos as referências
        marcadores_fim = ['apêndice', 'anexo', 'resumo'] 
        
        for marcador in marcadores_fim:
            # Encontra o primeiro marcador de fim no texto das referências e guarda seu indice
            indice_corte = referencias.lower().find(marcador)
            
            # Realiza o corte SÓ SE o marcador for encontrado bem depois do início da seção
            if indice_corte != -1 and indice_corte > 100: 
                referencias = referencias[:indice_corte].strip()
                break
                
    # Se match_end não foi encontrado, retorna a string vazia 
    return referencias

#---------------------------------------------------------------------------------------------------------------------#

# Trata o texto dividindo ele em paragrafos e retirando espaços inuteis
def dividir_em_paragrafos(texto_completo: str) -> List[str]:
    return [p.strip() for p in texto_completo.split('\n\n') if p.strip()] # quebra o texto em pagrafos e gera uma lista com eles.

#---------------------------------------------------------------------------------------------------------------------#

def identificar_objetivo(paragrafo: str) -> Optional[str]:

    if nlp is None: #verifica se o modelo usado foi iniciado corretamente
        return None
        
    # vetor com verbos que expressam intenção ou propósito.
    marcadores_objetivo = {"visar", "propor", "objetivar", "buscar", "analisar", "desenvolver", "apresentar", "estudar", "avaliar", "criticar", 
                           "questionar", "revisitar", "debater", "demonstrar", "provar","defender", "sustentar", "discutir", "examinar", "explorar",
                           "investigar", "tratar", "abordar"}
        
    # Foca nos primeiros 10 parágrafos, porque normalmente o objetivo já é descrito neles
    for paragrafo in paragrafos[:10]: 
        doc_paragrafo = nlp(paragrafo) #Passa o paragrafo para o modelo
        
        # procura um verbo de intenção na forma base (lema)
        for token in doc_paragrafo:
            if token.pos_ == "VERB" and token.lemma_ in marcadores_objetivo: # verifica se o lema do verbo que esta na lista esta presente no texto 
                return paragrafo # se ele estiver presente retorna o parágrafo inteiro
                    
    return None #garantia de que a função sempre ira retornar um valor, nem que seja nada (none).

#---------------------------------------------------------------------------------------------------------------------#

# Identifica o parágrafo que define a lacuna ou a questão de pesquisa, buscando termos que indicam limitação, contraste ou questão.
def identificar_problema(paragrafo: str) -> Optional[str]:
    
    if nlp is None: #verifica se o modelo usado foi iniciado corretamente
        return None

    # Palavras-chave que indicam uma questão, contraste ou limitação (problema)
    marcadores_problema = {"lacuna", "desafio", "questão", "problema", "limitação", "apesar", "entanto", "falta", "incerteza"}
    
    for paragrafo in paragrafos:
        texto_paragrafo_lower = paragrafo.lower()
        
        # Busca por marcadores de problema no texto em minúsculas
        if any(marcador in texto_paragrafo_lower for marcador in marcadores_problema):
            return paragrafo
            
    return None #garantia de que a função sempre ira retornar um valor, nem que seja nada (none).

#---------------------------------------------------------------------------------------------------------------------#

def identificar_contribuicao(paragrafos: str) -> Optional[str]:
 
    if nlp is None: #verifica se o modelo usado foi iniciado corretamente
        return None

    # Verbos/Substantivos que expressam contribuição, novidade ou impacto
    marcadores_contribuicao = {"contribuir", "inovar", "aprimorar", "superar", "resultado", "impacto", "abordagem", "novo", "inédito", "concluir", "evidenciar", "sugerir"}
    
    # procura em todo o texto 
    for paragrafo in paragrafos:
        doc_paragrafo = nlp(paragrafo) #passa o paragrafo pelo modelo usado, que retorna o texto em forma de token com informações 
        #linguisticas obtidas apos a analise realizada pelo modelo.
        for token in doc_paragrafo:
            if token.lemma_ in marcadores_contribuicao: # procura entre a lista de marcadores o lema do teken, se encontrado retorna o paragrafo correspondente
                return paragrafo
    return None #garantia de que a função sempre ira retornar um valor, nem que seja nada (none).

#---------------------------------------------------------------------------------------------------------------------#

def identificar_palavras_chaves(texto_completo: str) -> Optional[str]:
   
    if not texto_completo: #Verifica se a variavel texto_completo existe ou se esta vazia
        return None

    # Padrões comuns de marcadores em português e inglês (em minúsculas)
    marcadores = [
        r"palavras[ -]?chaves?", # Combina 'palavras-chave', 'palavras chave', 'palavra-chave', etc.
        r"keywords?" # Combina 'keyword' e 'keywords'.
    ] #usado para identificar cabeçalhos de seções, usado representações regulares para pegar as variações graficas
    
    texto_lower = texto_completo.lower()
    
    for marcador in marcadores:
        # Encontra o marcador seguido por um separador
        match = re.search(marcador + r"[\s:.-]*", texto_lower) #permite que o marcador seja seguido por pontuação e espaço
        
        if match:
            start_index = match.end()
            conteudo_restante = texto_completo[start_index:].strip()
            
            # Tenta isolar apenas a lista (até a próxima quebra de linha dupla ou simples)
            proxima_quebra = conteudo_restante.find('\n\n')
            
            if proxima_quebra != -1:
                return conteudo_restante[:proxima_quebra].strip()
            else:
                return conteudo_restante.split('\n')[0].strip()
                
    return None #garantia de que a função sempre ira retornar um valor, nem que seja nada (none).

#---------------------------------------------------------------------------------------------------------------------#

def resumir_texto(texto_completo: str) -> Optional[str]:
    
    if not texto_completo:
        return None
    
    parser = PlaintextParser.from_string(texto_completo, Tokenizer("portuguese")) #estrutura o texto para ser resumido de forma que o sumy reconheça
    
    summarizer = TextRankSummarizer() #seleciona e inicializa o algoritmo de resumo que será utilizado
    
    resumo_extrativo = summarizer(parser.document, sentences_count=5) #executa o algoritmo de resumo e o orienta a retornar as 5 frases raqueadas como mais importantes.
    
    resumo_final = " ".join([str(sentence) for sentence in resumo_extrativo]) #formatar e retornar o resumo como uma única string
    return resumo_final

#---------------------------------------------------------------------------------------------------------------------#

# Troque este caminho pelo caminho do PDF
CAMINHO_DO_SEU_PDF = r"CAMINHO DO ARQUIVO PDF" # <---------------------------------------

if __name__ == "__main__": #O que esta abaixo é executado somente se esse for o programa principal.
    
    # Extrai o texto do PDF
    texto_extraido = extrair_texto_completo_do_pdf(CAMINHO_DO_SEU_PDF)
    
    if "Erro" in texto_extraido or "Não foi possível" in texto_extraido:
               print("ERRO NA EXTRAÇÃO DO PDF")
        
    else:
        # Remove as stopwords do texto extraído
        texto_sem_stopwords = remover_stopwords(texto_extraido, STOPWORDS_PT)
        top_10 = calcular_frequencia_top_n(texto_sem_stopwords, n=10)

        print("-"*50)
        print("10 PALAVRAS MAIS FREQUÊNTES")
        print("-"*50)
        for palavra, frequencia in top_10:
            print(f"- {palavra}: {frequencia} ocorrências")

        referencias_extraidas = extrair_referencias_do_texto(texto_extraido)
        print()
        print("-"*50)
        print("REFERÊNCIAS EXTRAÍDAS")
        print("-"*50)
        if referencias_extraidas:
            print(referencias_extraidas)
        else:
            print("Nenhuma referência foi extraída.")

        paragrafos = dividir_em_paragrafos(texto_extraido)

        print()
        print("-"*50)
        print("PARÁGRAFOS CHAVE IDENTIFICADOS")
        print("-"*50)

        objetivo = identificar_objetivo(paragrafos)
        if not objetivo:
            print("1. Objetivo: não encontrado.")
        else:
            print(f"1. Objetivo:\n{objetivo}\n")

        print("-" * 20)

        problema = identificar_problema(paragrafos)
        if not problema:
            print("2. Problema: não encontrado.")
        else:
            print(f"2. Problema:\n{problema}\n")

        print("-" * 20)

        contribuicao = identificar_contribuicao(paragrafos)
        if not contribuicao:
            print("3. Contribuição: não encontrado.")
        else:
            print(f"3. Contribuição:\n{contribuicao}\n")
       
        print("-" * 20)

        palavra_chave = identificar_palavras_chaves(texto_extraido)
        if not palavra_chave:
            print("4. Palavras-chaves: não encontrado.")
        else:
            print(f"4. Palavras-chaves:\n{palavra_chave}\n")

        resumo = resumir_texto(texto_extraido)

        print()
        print("-"*50)
        print("RESUMO DO TEXTO")
        print("-"*50)

        print(resumo)
        print("="*60)