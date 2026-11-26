# Gerenciador de Despesas Pessoais

Aplicação desenvolvida em **Clojure** como parte do trabalho acadêmico *Explorando Paradigmas de Programação*, com o objetivo de demonstrar a aplicação prática dos conceitos da Programação Funcional.

O sistema permite cadastrar, consultar, filtrar e analisar despesas pessoais por meio de um menu interativo executado no terminal.

## 1. Tecnologias utilizadas

- **Linguagem:** Clojure 1.12.0
- **Plataforma:** Java Virtual Machine (JVM)
- **Gerenciamento de dependências:** Clojure CLI (deps.edn)
- **Bibliotecas:** Java BigDecimal e java.time para operações numéricas e manipulação de datas.

## 2. Funcionalidades

O sistema disponibiliza as seguintes operações:

1. **Listar despesas:** apresenta todas as despesas cadastradas.
2. **Cadastrar despesa:** permite inserir uma nova despesa com descrição, categoria, valor e data.
3. **Filtrar por categoria:** seleciona despesas pertencentes a uma categoria específica.
4. **Filtrar por período:** consulta despesas dentro de um intervalo de datas.
5. **Filtrar por valor mínimo:** apresenta despesas com valores iguais ou superiores ao informado.
6. **Consultar total de gastos:** calcula a soma de todas as despesas.
7. **Relatório por categoria:** agrupa as despesas e apresenta os totais de cada categoria.
8. **Resumo financeiro:** apresenta a quantidade de despesas, o total gasto, a média dos valores e a maior despesa.

## 3. Instalação e configuração do ambiente

As instruções a seguir consideram o sistema operacional Windows.

#### 3.1. Instalação do Java JDK

O Clojure utiliza a Java Virtual Machine (JVM), portanto é necessário instalar o Java JDK antes de configurar o ambiente.

1. Acesse o site oficial da [Oracle Java Downloads](https://www.oracle.com/java/technologies/downloads/).
2. Selecione a versão **JDK 25 (LTS)**.
3. Na seção Windows, escolha o instalador **x64 MSI Installer**.
4. Baixe e execute o arquivo `.msi`.
5. Siga as instruções do instalador, mantendo as configurações padrão.
6. Após a instalação, abra um novo terminal e execute:

```bash
java -version
```

Se as informações da versão do Java forem apresentadas, a instalação foi concluída.

### 3.2. Instalação do Clojure CLI

Após instalar o Java, é necessário configurar o Clojure CLI, responsável pela execução dos programas e pelo gerenciamento das dependências.

1. Acesse a página de [instalação do Clojure](https://clojure.org/guides/install_clojure).
2. Na seção Windows Installer, acesse os [instaladores Clojure MSI](https://github.com/casselc/clj-msi/releases).
3. Baixe a versão mais recente do instalador `.msi`.
4. Execute o arquivo baixado e siga as instruções de instalação.
5. Abra um novo terminal e execute:

```bash
clojure -Sdescribe
```

Se as informações de configuração do Clojure CLI forem apresentadas, a instalação foi concluída.

## 4. Pré-requisitos

Antes de executar a aplicação, é necessário ter instalado:

- Java JDK 21 ou compatível;
- Clojure CLI;

## 5. Como executar

**1. Baixar o projeto**

Acesse a pasta [Gerenciador de Despesas no GitHub](https://github.com/RayssaMCC/Unespar/tree/main/4_Ano/Ling_Prog/Clojure/gerenciador-despesas).

Para baixar somente os arquivos do projeto, utilize o
[GitHub Folder Downloader](https://githubfolder.com/),
cole o endereço da pasta e clique em Download ZIP.

**2. Extrair os arquivos**

Extraia o conteúdo do arquivo ZIP para uma pasta no computador.

**3. Abrir o terminal na pasta do projeto**

Acesse a pasta extraída, onde estão os arquivos `deps.edn` e `src`.

**4. Executar a aplicação**

```bash
clojure -M:run
```

Após a execução, o menu principal será apresentado no terminal.

## 6. Utilização do sistema

O usuário pode selecionar uma das opções disponíveis digitando o número correspondente no menu.

Cada despesa possui quatro atributos:

- **Descrição:** identificação do gasto.
- **Categoria:** classificação da despesa.
- **Valor:** quantia correspondente ao gasto.
- **Data:** dia em que a despesa ocorreu.

Para o cadastro, o valor deve ser informado utilizando ponto como separador decimal, quando necessário (exemplo: `150.50`), e a data deve seguir o formato `DD-MM-AAAA` (exemplo: `26-11-2026`).

As categorias devem ser informadas com o mesmo texto utilizado no cadastro, respeitando maiúsculas, minúsculas e acentuação.

## 7. Conceitos da Programação Funcional aplicados

Durante o desenvolvimento, foram utilizados diferentes recursos da linguagem Clojure para demonstrar os princípios do paradigma funcional:

- **Funções:** organização das operações em funções independentes e reutilizáveis.
- **Imutabilidade:** utilização de `conj` para gerar um novo vetor ao adicionar despesas, preservando a coleção anterior.
- **Funções de alta ordem:** utilização de `map` e `filter` para transformar e selecionar elementos das coleções.
- **Redução:** utilização de `reduce` para acumular os valores das despesas e calcular os totais.
- **Composição de funções:** utilização da macro `->>` para encadear operações na geração de relatórios.
- **Recursão:** utilização de `recur` para repetir a execução do menu principal.

Esses recursos permitem organizar o processamento das informações por meio de transformações de dados, mantendo a separação entre as operações e a interação com o usuário.

## 8. Observações

Os registros iniciais são definidos diretamente no código-fonte. As despesas cadastradas durante a execução permanecem armazenadas em memória e não são salvas permanentemente. Portanto, ao encerrar e iniciar novamente a aplicação, os registros retornam aos dados iniciais.

---

**Trabalho acadêmico:** Explorando Paradigmas de Programação  
**Paradigma:** Programação Funcional  
**Linguagem:** Clojure  
**Alunos:** Guilherme Fortunato da Silva, Paloma de Castro Leite, Rayssa Mara Caldini Costa
