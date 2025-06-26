#include <iostream>
#include <iomanip> // Para formatação da saída
#include <fstream>
#include <sstream>
#include <vector>
#include <cctype>
#include <iomanip>
#include <unordered_set> // Mais rápido que vector para busca e ignora duplicatas
#include <string>
using namespace std;

// --- Estruturas e Variáveis Globais ---
struct Token {
    string lexema;
    string tipo;
    int linha;
};

struct NoSintatico {
    string tipo;
    string valor;
    vector<NoSintatico*> filhos;
    NoSintatico(string tipo, string valor = "") : tipo(tipo), valor(valor) {}
    ~NoSintatico() {
        for (auto filho : filhos) {
            delete filho;
        }
    }
};

vector<Token> tokens;
int pos = 0;

Token atual() {
    if(pos < (int)tokens.size()) return tokens[pos];
    return Token{"", "EOF", -1};
}

void avancar() {
    if(pos < (int)tokens.size()) pos++;
}

// --- Analisador Léxico ---
static unordered_set<string> palavrasReservadas = {
    "Program", "read", "write", "integer", "boolean", "double", "function", "procedure", "begin", "end",
    "and", "array", "case", "const", "div", "do", "downto", "else", "file", "for", "goto", "if", "in",
    "label", "mod", "nil", "not", "of", "or", "packed", "record", "repeat", "set", "then", "to",
    "type", "until", "with", "var", "while"
};

bool isPalavraReservada(const string& palavra) { //& é pra referência, parecido com ponteiro
    return palavrasReservadas.count(palavra) > 0;
}

bool isSimboloSimples(char c) {
    static const unordered_set<char> simbolos = {'^', '*', '=', '.', ';', ',', '[', ']', '(', ')'};
    return simbolos.count(c) > 0;
}

void analisar(string& codigo) {
    size_t i = 0; //codigo.length retorna um size_t, então pra comparar é melhor usar o mesmo tipo
    int linha = 1;

    while(i < codigo.length()) {
        char c = codigo[i];

        // Comentários de linha //
        if(c == '/' && i+1 < codigo.length() && codigo[i+1] == '/') {
            i += 2; // pula os dois caracteres: //
            while(i < codigo.length() && codigo[i] != '\n') i++;
            continue;
        }

        // Comentários bloco (* *)
        if(c == '(' && i+1 < codigo.length() && codigo[i+1] == '*') {
            i += 2; // pula os dois caracteres: (*
            while(i+1 < codigo.length() && !(codigo[i] == '*' && codigo[i+1] == ')')) {
                if(codigo[i] == '\n') linha++;
                i++;
            }
            if(i+1 < codigo.length()) i += 2; // pula o *)
            continue;
        }

        // Comentários bloco { }
        if(c == '{') {
            i++;
            while(i < codigo.length() && codigo[i] != '}') {
                if(codigo[i] == '\n') linha++;
                i++;
            }
            if(i < codigo.length()) i++; // pula o }
            continue;
        }

        if(c == '\n') { // Atualiza contador de linhas
            linha++;
            i++;
            continue;
        }

        if(isspace(c) && c != '\n') { // Ignora espaços em branco
            i++;
            continue;
        }

        // E1 → E2 (Identificador ou palavra reservada)
        if (isalpha(c)) {
            string lexema;
            lexema += c;
            i++;

            // E2 → E2 (letras e Numeros)
            while (i < codigo.length() && isalnum(codigo[i])) {
                lexema += codigo[i++];
            }

            // Verifica se é palavra reservada ou identificador
            string tipo = isPalavraReservada(lexema) ? "Palavra Reservada" : "Identificador";
            tokens.push_back({lexema, tipo, linha});

        }
        // E1 → E3 → E4 (Numero inteiro ou real)
        else if (isdigit(c)) {
            string numero;
            numero += c;
            i++;

            while (i < codigo.length() && isdigit(codigo[i])) {
                numero += codigo[i++];
            }

            // Verifica se é Numero com ponto decimal
            if (i < codigo.length() && codigo[i] == '.' && i + 1 < codigo.length() && isdigit(codigo[i + 1])) {
                numero += codigo[i++]; // adiciona ponto
                while (i < codigo.length() && isdigit(codigo[i])) {
                    numero += codigo[i++];
                }
            }

            tokens.push_back({numero, "Numero", linha});
        }

        // E1 → E7/E9/E11/E13/E15 → E8/E10/E12/E14/E16 (Simbolos compostos)
        else if ((c == '<' || c == '>' || c == '+' || c == '-' || c == ':') && i + 1 < codigo.length()) {
            char prox = codigo[i + 1];
            string composto = string(1, c) + prox; //string de 1 caractere com o valor de c + o próximo caractere

            if (composto == "<=" || composto == "<>" || composto == ">=" || composto == "++" || composto == "--" || composto == ":=") {
                tokens.push_back({composto, "Simbolo Composto", linha});
                i += 2; // avança 2 posições pois já processou os dois caracteres
            } else {
                tokens.push_back({string(1, c), "Simbolo Simples", linha});  // E7/E9/E11/E13/E15 (apenas Simbolos simples que iniciam um composto)
                i++;
            }
        }

        // E1 → E6 (Simbolos simples: ^ * = . ; , ( ) [ ] )
        else if (isSimboloSimples(c)) {
            tokens.push_back({string(1, c), "Simbolo Simples", linha});
            i++;
        }

        // E1 → ? (Erro léxico)
        else {
            cout << "Erro lexico: linha " << linha << " - Caractere invalido '" << c << "'\n";
            i++;
        }
    }
}

int criarTabela(){
    ifstream entrada("entrada.txt"); // abre arquivo de entrada
    ofstream saida("tabela_simbolos.txt"); // cria arquivo de saída

    if (!entrada.is_open()) {
        cerr << "Erro ao abrir entrada.txt\n";
        return 1;
    }

    if (!saida.is_open()) {
        cerr << "Erro ao criar tabela_simbolos.txt\n";
        return 1;
    }

    stringstream buffer;
    buffer << entrada.rdbuf(); // lê conteúdo do arquivo de entrada todo para buffer
    string codigo = buffer.str(); // armazena como string

    analisar(codigo);

    saida << left << setw(10) << "Linha" << setw(20) << "Lexema" << setw(25) << "Tipo" << "\n";
    saida << string(55, '-') << "\n";

    for (const Token& token : tokens) {
        saida << left << setw(10) << token.linha << setw(20) << token.lexema << setw(25) << token.tipo << "\n";
    }

    cout << "Analise lexica concluida. Veja o arquivo: tabela_simbolos.txt\n";

    entrada.close();
    saida.close();

    return 0;
}

// --- ANALISADOR SINTÁTICO ---
NoSintatico* programa();
NoSintatico* bloco();
NoSintatico* comando();
NoSintatico* comandoSemRotulo();
NoSintatico* expressao();
NoSintatico* expressaoSimples();
NoSintatico* termo();
NoSintatico* fator();
NoSintatico* tipo();
NoSintatico* parametrosFormais();

NoSintatico* terminal(const string& tipo, const string& valor = "") {
    if (atual().tipo == tipo && (valor.empty() || atual().lexema == valor)) {
        NoSintatico* no = new NoSintatico(tipo, atual().lexema);
        avancar();
        return no;
    }
    return nullptr;
}

NoSintatico* programa() {
    NoSintatico* noPrograma = new NoSintatico("programa"); //no Raiz.

    NoSintatico* no = terminal("Palavra Reservada", "Program");
    if (!no){ 
        delete noPrograma; 
        cout<<"Erro sintatico: funcao prorama 'Programa'\n";
        return nullptr; 
    }
    noPrograma->filhos.push_back(no);

    NoSintatico* id = terminal("Identificador");
    if (!id){ 
        delete noPrograma; 
        cout<<"Erro sintatico: funcao programa espera-se o 1 id\n";
        return nullptr; 
    }
    noPrograma->filhos.push_back(id);
    
    NoSintatico* simbSimples = terminal("Simbolo Simples", "(");
    if (simbSimples){
        noPrograma->filhos.push_back(simbSimples);
        // Lógica para lista de identificadores (input, output)
        if (atual().tipo == "Identificador") {
            noPrograma->filhos.push_back(terminal("Identificador"));
            while(terminal("Simbolo Simples", ",")) {
                noPrograma->filhos.push_back(terminal("Simbolo Simples", ","));
                NoSintatico* id_lista = terminal("Identificador");
                if(!id_lista){ 
                    delete noPrograma; 
                    return nullptr; 
                }
                noPrograma->filhos.push_back(id_lista);
            }
        }else{
            delete noPrograma;
            cout<< "Erro sintatico: funcao programa, espera-se um id apos (\n";
            return nullptr;
        }
        NoSintatico* simbSimples2 = terminal("Simbolo Simples", ")");
        if (!simbSimples2){ 
            delete noPrograma; 
            cout<< "Erro sintatico: funcao programa, espera-se um )\n";
            return nullptr; 
        }
        noPrograma->filhos.push_back(simbSimples2);
    }

    NoSintatico* pontoVirgula = terminal("Simbolo Simples", ";");
    if (!pontoVirgula){ 
        delete noPrograma; 
        cout<< "Erro sintatico: funcao programa, espera-se ; apos o id\n";
        return nullptr; 
    }
    noPrograma->filhos.push_back(pontoVirgula);
    
    NoSintatico* noBloco = bloco();
    if (!noBloco){ 
        delete noPrograma; 
        cout<< "Erro sintatico: funcao programa, erro ao percorrer bloco\n";
        return nullptr; 
    }
    no->filhos.push_back(noBloco);

    NoSintatico* ponto = terminal("Simbolo Simples", ".");
    if (!ponto){ 
        delete noPrograma; 
        cout<< "Erro sintatico: funcao programa, espera-se .\n";
        return nullptr; 
    }
    noPrograma->filhos.push_back(ponto);
    return noPrograma;
}

NoSintatico* bloco() {
    NoSintatico* noBloco = new NoSintatico("Bloco");

    if (!(atual().lexema == "label" || atual().lexema == "type" || atual().lexema == "var" ||
          atual().lexema == "procedure" || atual().lexema == "function" || atual().lexema == "begin")) {
        delete noBloco;
        cout<< "Erro sintatico: espera-se label, type, var, procedure, function ou begin\n";
        return nullptr;
    }

    if(atual().lexema == "label"){
        noBloco->filhos.push_back(terminal("Palavra Reservada", "label"));
        NoSintatico* num = terminal("Numero");
        if(!num){
            delete noBloco;
            cout<<"Erro sitatico: funcao bloco 'label' espera-se um Numero\n";
            return nullptr;
        }
        noBloco->filhos.push_back(num);

        while(true){
            if(atual().lexema != ",") break;
            noBloco->filhos.push_back(terminal("Simbolo Simples", ","));
            NoSintatico* num2 = terminal("Numero");
            if(!num2){
                delete noBloco;
                cout<<"Erro sintatico: fucao Bloco, espera-se um Numero apos a ,\n";
                return nullptr;
            }
            noBloco->filhos.push_back(num2);
        }

        NoSintatico* pontoVirgula = terminal("Simbolo Simples", ";");
        if(!pontoVirgula){
            delete noBloco;
            cout<<"Erro sintatico: funcao Bloco label, espera-se um ;\n";
            return nullptr;
        }
        noBloco->filhos.push_back(pontoVirgula);
    }

    if(atual().lexema == "type"){
        noBloco->filhos.push_back(terminal("Palavra Reservada"));

        do{
            NoSintatico* id = terminal("Identificador");
            if(!id){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco type, espera-se um Identificador, apos o type\n";
                return nullptr;
            }
            noBloco->filhos.push_back(id);

            NoSintatico* igual = terminal("Simbolo Simples", "=");
            if(!igual){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco type, espera-se um = apos o id\n";
                return nullptr;
            }
            noBloco->filhos.push_back(igual);

            NoSintatico* noTipo = tipo();
            if(!noTipo){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco type, percorre tipo() deu erro\n";
                return nullptr;
            }
            noBloco->filhos.push_back(noTipo);

            NoSintatico* pontoVirgula = terminal("Simbolo Simples", ";");
            if(!pontoVirgula){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco type, espera-se ; apos tipo()\n";
                return nullptr;
            }
            noBloco->filhos.push_back(pontoVirgula);
        }while(atual().tipo == "Identificador");
    }
    
    if(atual().lexema == "var"){
        noBloco->filhos.push_back(terminal("Palavra Reservada"));

        do{
                NoSintatico* id = terminal("Identificador");
            if(!id){
                delete noBloco;
                cout<< "Erro sintatico: funcao Bloco var, espera-se um id\n";
                return nullptr;
            }
            noBloco->filhos.push_back(id);

            while(atual().lexema == ","){
                noBloco->filhos.push_back(terminal("Simbolo Simples", ","));
                NoSintatico* id2 = terminal("Identificador");
                if(!id2){
                    delete noBloco;
                    cout<< "Erro sintatico: funcao Bloco var, espera-se um id apos a ,\n";
                    return nullptr;
                }
                noBloco->filhos.push_back(id2);
            }

            NoSintatico* doisPontos = terminal("Simbolo Simples", ":");
            if(!doisPontos){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco var, espera-se : apos o id\n";
                return nullptr;
            }
            noBloco->filhos.push_back(doisPontos);

            NoSintatico* blocoTipo = tipo();
            if(!blocoTipo){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco var, erro ao executar tipo()\n";
                return nullptr;
            }
            noBloco->filhos.push_back(blocoTipo);

            NoSintatico* pontoVirgula = terminal("Simbolo Simples", ";");
            if(!pontoVirgula){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco, espera-se um ; apos tipo()\n";
                return nullptr;
            }
            noBloco->filhos.push_back(pontoVirgula);
        }while(atual().tipo == "Identificador");
    }

    while(atual().lexema == "procedure" || atual().lexema == "function"){
        string palavra = atual().lexema;
        noBloco->filhos.push_back(terminal("Palavra Reservada"));

        NoSintatico* id = terminal("Identificador");
        if(!id){
            delete noBloco;
            cout<<"Erro sintatico: funcao Bloco procedure/function, espera-se um id\n";
            return nullptr;
        }
        noBloco->filhos.push_back(id);

        if(palavra == "procedure"){
            NoSintatico* blocoParametrosFormais = parametrosFormais();
            if(blocoParametrosFormais){
                noBloco->filhos.push_back(blocoParametrosFormais);
            }
        }else{
            NoSintatico* blocoParametrosFormais = parametrosFormais();
            if(blocoParametrosFormais){
                noBloco->filhos.push_back(blocoParametrosFormais);
            }

            NoSintatico* doisPontos = terminal("Simbolo Simples");
            if(!doisPontos){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco function, espera-se : apos o id ou parametrosFormais()\n";
                return nullptr;
            }
            noBloco->filhos.push_back(doisPontos);

            NoSintatico* tipoDeRetorno = tipo(); //pra resolver problemas como: function SomaSePar(a, b: integer): integer;
            if(!tipoDeRetorno){
                delete noBloco;
                cout<<"Erro sintatico: funcao Bloco function, tipo de retorno da funcao e invalido.\n";
                return nullptr;
            }
            noBloco->filhos.push_back(tipoDeRetorno);
        }

        NoSintatico* pontoVirgula = terminal("Simbolo Simples", ";");
        if(!pontoVirgula){
            delete noBloco;
            cout<<"Erro sintatico: funcao Bloco procedure/function, espera-se ; apos id\n";
            return nullptr;
        }
        noBloco->filhos.push_back(pontoVirgula);

        NoSintatico* blocoRec = bloco();
        if(!blocoRec){
            delete noBloco;
            cout<<"Erro sintatico: funcao Bloco procedure/function, erro ao executar recursao de bloco()\n";
            return nullptr;
        }
        noBloco->filhos.push_back(blocoRec);

        NoSintatico* doisPontos = terminal("Simbolo Simples", ";");
        if(!doisPontos){
            delete noBloco;
            cout<<"Erro sintatico: funcao Bloco procedure/function, epera-se ; apos bloco()\n";
            return nullptr;
        }
        noBloco->filhos.push_back(doisPontos);
    }

    if (atual().lexema == "begin") {
        noBloco->filhos.push_back(terminal("Palavra Reservada"));
        NoSintatico* cmd = comando();
        if (!cmd) { 
            delete noBloco; 
            return nullptr; 
        }
        noBloco->filhos.push_back(cmd);
        while(atual().lexema == ";") {
            noBloco->filhos.push_back(terminal("Simbolo Simples", ";"));
            cmd = comando();
            if (!cmd) { 
                delete noBloco; 
                cout<<"Erro sintatico: funcao Bloco, erro ao executar comando()\n";
                return nullptr; 
            }
            noBloco->filhos.push_back(cmd);
        }
        if (!terminal("Palavra Reservada", "end")) { 
            delete noBloco; 
            return nullptr; 
        }
        return noBloco;
    }
}

NoSintatico* tipo() {
    NoSintatico* noTipo = new NoSintatico("Tipo");

    if (atual().lexema == "array") {
        noTipo->filhos.push_back(terminal("Palavra Reservada"));

        NoSintatico* abreColchete = terminal("Simbolo Simples");
        if(!abreColchete){
            delete noTipo;
            cout<<"Erro sintatico: funcao Tipo array, espera-se um [\n";
            return nullptr;
        }

        while(atual().tipo == "Numero"){
            NoSintatico* num = terminal("Numero");

            if(!num){
                delete noTipo;
                cout<<"Erro sintatico: fucao Tipo array, espera-se um Numero apos [\n";
                return nullptr;
            }
            noTipo->filhos.push_back(num);
            
            NoSintatico* ponto1 = terminal("Simbolo Simples", ".");
            if(!ponto1){
                delete noTipo;
                cout<<"Erro sintatico: funcao Tipo array, espera-se .";
                return nullptr;
            }
            noTipo->filhos.push_back(ponto1);

            NoSintatico* ponto2 = terminal("Simbolo Simples", ".");

            if(!ponto2){
                delete noTipo;
                cout<<("Erro sintatico: funcao Tipo, espera-se . depois de .\n");
                return nullptr;
            }
            noTipo->filhos.push_back(ponto2);

            NoSintatico* num2 = terminal("Numero");
            if(!num2){
                delete noTipo;
                cout<<"Erro sintatico: funcao Tipo, espera-se um Numero apos ..\n";
                return nullptr;
            }
            noTipo->filhos.push_back(num2);
        }
        
        NoSintatico* fechaColchete = terminal("Simbolo Simples", "]");
        if(!fechaColchete){
            delete noTipo;
            cout<<"Erro sintatico: funcao Tipo, espera-se ]\n";
            return nullptr;
        }
        noTipo->filhos.push_back(fechaColchete);

        NoSintatico* of = terminal("Palavra Reservada");
        if(!of){
            delete noTipo;
            cout<<"Erro sintatico: funcao Tipo, espera-se 'of'\n";
            return nullptr;
        }
        noTipo->filhos.push_back(of);

        NoSintatico* tipoRec = tipo();
        if(!tipoRec){
            delete noTipo;
            cout<<"Erro sintatico: funcao Tipo, erro de recursao\n";
            return nullptr;
        }
        noTipo->filhos.push_back(tipoRec);
        return noTipo;
    }

    //Se não for array, verifica se é um tipo primitivo (não tem no diagrama mas não funcionaria sem essa especificação)
    else if (atual().tipo == "Palavra Reservada" && (atual().lexema == "integer" || atual().lexema == "boolean" || atual().lexema == "double")) {
        noTipo->filhos.push_back(terminal("Palavra Reservada"));
        return noTipo;
    } 
    //Se não, verifica se é um identificador (tipo customizado)
    else if (atual().tipo == "Identificador") {
        noTipo->filhos.push_back(terminal("Identificador"));
        return noTipo;
    } 
    else {
        delete noTipo;
        cout << "Erro sintatico: funcao Tipo, espera-se 'array', um identificador de tipo ou um tipo primitivo (integer, boolean, etc.).\n";
        return nullptr;
    }
}


NoSintatico* parametrosFormais(){
    NoSintatico* noParametrosFormais = new NoSintatico("Parametros Formais");

    NoSintatico* abreParenteses = terminal("Simbolo Simples", "(");
    if(!abreParenteses){
        delete noParametrosFormais;
        cout<<"Erro sintatico: funcao Parametros Formais, espera-se (\n ";
        return nullptr;
    }
    noParametrosFormais->filhos.push_back(abreParenteses);

    do{
        string palavra = atual().lexema;
       if(atual().lexema == "var"){
           noParametrosFormais->filhos.push_back(terminal("Palavra Reservada"));
        }

        if(atual().lexema == "function" && (tokens[pos-1].lexema == "(" || tokens[pos-1].lexema == ";")){
            noParametrosFormais->filhos.push_back(terminal("Palavra Reservada"));
        }else if(atual().lexema == "procedure" && (tokens[pos-1].lexema == "(" || tokens[pos-1].lexema == ";")){
            noParametrosFormais->filhos.push_back(terminal("Palavra Reservada"));
        }else if((atual().lexema == "function" && (tokens[pos-1].lexema != "(" && tokens[pos-1].lexema != ";")) || (atual().lexema == "procedure" && (tokens[pos-1].lexema != "(" && tokens[pos-1].lexema != ";"))){
            delete noParametrosFormais;
            cout<<"Erro sintatco: funcao Paramentos Formais, uso indevido da palavra function ou procedure\n";
            return nullptr;
        }

        NoSintatico* id = terminal("Identificador");
        if(!id){
            delete noParametrosFormais;
            cout<<"Erro sintatico: funcao Paramentros Formais, espera-se um id\n";
            return nullptr;
        }
        noParametrosFormais->filhos.push_back(id);

        while(atual().lexema == ","){
            noParametrosFormais->filhos.push_back(terminal("Simbolo Simples", ","));

            NoSintatico* id2 = terminal("Identificador");
            if(!id2){
                delete noParametrosFormais;
                cout<<"Erro sintatico: funcao Paramentros Formais, espera-se um id\n";
                return nullptr;
            }
            noParametrosFormais->filhos.push_back(id2);
        }

        if(palavra == "procedure"){
            NoSintatico* pontoVirgula = terminal("Simbolo Simples", ";");
            if(!pontoVirgula){
                delete noParametrosFormais;
                cout<<"Erro sintatico: funcao Parametros Formais procedure, epera-se ; apos id\n";
                return nullptr;
            }
            noParametrosFormais->filhos.push_back(pontoVirgula);
        }else{
            NoSintatico* doisPontos = terminal("Simbolo Simples", ":");
            if(!doisPontos){
                delete noParametrosFormais;
                cout<<"Erro sinatatico: funcao Parametros Formais var/function/id, espera-se : apos o id\n";
                return nullptr;
            }
            noParametrosFormais->filhos.push_back(doisPontos);

            NoSintatico* tipoParametro = tipo();
            if(!tipoParametro){
                delete noParametrosFormais;
                cout<<"Erro sintatico: funcao Parametros Formais, tipo de parametro invalido ou nao reconhecido.\n";
                return nullptr;
            }
            noParametrosFormais->filhos.push_back(tipoParametro);;

            NoSintatico* pontoVirgula = terminal("Simbolo Simples", ";");
            if(pontoVirgula){
                noParametrosFormais->filhos.push_back(pontoVirgula);
            }
        }
    }while(atual().lexema != ")");

    NoSintatico* fechaParenteses = terminal("Simbolo Simples", ")");
    if(!fechaParenteses){
        delete noParametrosFormais;
        cout<<"Erro sintatico: funcao Parametros Formais, espera-se )\n";
        return nullptr;
    }else{
        noParametrosFormais->filhos.push_back(fechaParenteses);
        return noParametrosFormais;
    }
}

NoSintatico* comando() { //usa lookahead para verificar se o comando tem rotulo ou não, com backtracking quebrava
    if (atual().tipo == "Numero" && tokens[pos + 1].lexema == ":") { 
        NoSintatico* rotulo = terminal("Numero");
        NoSintatico* doisPontos = terminal("Simbolo Simples", ":");

        NoSintatico* cmdAposRotulo = comandoSemRotulo();
        if (!cmdAposRotulo) {
            cout << "Erro sintatico: O rotulo '" << rotulo->valor << "' nao e seguido por um comando valido.\n";
            delete rotulo;
            delete doisPontos;
            return nullptr;
        }
        NoSintatico* noComandoComRotulo = new NoSintatico("ComandoComRotulo");
        noComandoComRotulo->filhos.push_back(rotulo);
        noComandoComRotulo->filhos.push_back(doisPontos);
        noComandoComRotulo->filhos.push_back(cmdAposRotulo);
        return noComandoComRotulo;

    } else {
        return comandoSemRotulo();
    }
}

NoSintatico* comandoSemRotulo() {
    int checkpoint = pos;

    NoSintatico* noComandoSemRotulo = new NoSintatico("Comando Sem Rotulo");

    if (atual().tipo == "Identificador") {
         noComandoSemRotulo->filhos.push_back(terminal("Identificador"));

        if (atual().lexema == ":=" || atual().lexema == "[") {
            if(atual().lexema == "["){
                noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", "["));

                NoSintatico* noExpressao = expressao();
                if(!noExpressao){
                    delete noComandoSemRotulo;
                    pos = checkpoint;
                    cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro na execução da expressão apos [ \n";
                    return nullptr;
                }
                noComandoSemRotulo->filhos.push_back(noExpressao);

                while(atual().lexema == ","){
                    noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", ","));

                    NoSintatico* noExpressao3 = expressao();
                    if(!noExpressao3){
                        delete noComandoSemRotulo;
                        pos = checkpoint;
                        cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro ao processar expressao apos ,\n";
                        return nullptr;
                    }
                    noComandoSemRotulo->filhos.push_back(noExpressao3);
                }

                if(atual().lexema == "]"){
                    noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", "]"));
                }else{
                    delete noComandoSemRotulo;
                    pos = checkpoint;
                    cout<<"Erro sintatico: funcao Comando sem Rotulo id, espera-se ]\n";
                    return nullptr;
                }
            }

            NoSintatico* doisPontosIgual = terminal("Simbolo Composto", ":=");
            if(!doisPontosIgual){
                delete noComandoSemRotulo;
                pos = checkpoint;
                cout<<"Erro sintatico: funcao Comando sem Rotulo id, espera-se := apos id/]"<< atual().lexema << "   " << tokens[pos-1].lexema << "\n";
                return nullptr;
            }
            noComandoSemRotulo->filhos.push_back(doisPontosIgual);

            NoSintatico* noExpressao1 = expressao();
            if (!noExpressao1) {
                delete noComandoSemRotulo;
                pos = checkpoint;
                cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro ao executar expressao() apos :=\n";
                return nullptr;
            }
            noComandoSemRotulo->filhos.push_back(noExpressao1);
            return noComandoSemRotulo;

        } else if (atual().lexema == "(") {
            noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", "("));

            NoSintatico* noExpressao1 = expressao();
            if(!noExpressao1){
                delete noComandoSemRotulo;
                cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro em execução de expressao() apos (\n";
                return nullptr;
            }
            noComandoSemRotulo->filhos.push_back(noExpressao1);

            while (atual().lexema == ",") { // se houver mais de um parâmetro
                noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", ","));

                NoSintatico* noExpressao2 = expressao();
                if(!noExpressao2) { 
                    delete noComandoSemRotulo;
                    pos = checkpoint; 
                    cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro em execução de expressao() apos ,\n";
                    return nullptr;
                }
                noComandoSemRotulo->filhos.push_back(noExpressao2);
            }

            NoSintatico* fechaParenteses = terminal("Simbolo Simples", ")");
            if(fechaParenteses){
                noComandoSemRotulo->filhos.push_back(fechaParenteses);
                return noComandoSemRotulo;
            }else{
                delete noComandoSemRotulo;
                pos = checkpoint;
                cout<<"Erro sintatico: funcao Comando sem Rotulo id, espera-se )\n";
                return nullptr;
            }
        }
        return noComandoSemRotulo;

    }else if (atual().lexema == "if") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));
        NoSintatico* noExpressao = expressao();

        if (noExpressao) {
            noComandoSemRotulo->filhos.push_back(noExpressao);

            if(atual().lexema == "then"){
                noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));

                NoSintatico* noComandoSemRotuloRec = comandoSemRotulo();
                if (noComandoSemRotuloRec) {
                    noComandoSemRotulo->filhos.push_back(noComandoSemRotuloRec);
                    NoSintatico* palavraElse = terminal("Palavra Reservada", "else");
                    if (palavraElse) {
                        noComandoSemRotulo->filhos.push_back(palavraElse);
                        NoSintatico* cmdElse = comandoSemRotulo();
                        if (!cmdElse) { 
                            delete noComandoSemRotulo; 
                            pos = checkpoint;
                            cout<<"Erro sintatico: funcao Comando sem Rotulo if, erro na recursao\n"; 
                            return nullptr; 
                        }
                        noComandoSemRotulo->filhos.push_back(cmdElse);
                    }
                    return noComandoSemRotulo;
                }else {
                    delete noComandoSemRotulo;
                    pos = checkpoint;
                    cout<<"Erro sintatico: funcao Comando sem Rotulo if, erro no comando apos 'then'\n";
                    return nullptr;
                }
            }else {
                // Erro: Esperava 'then'
                delete noComandoSemRotulo;
                pos = checkpoint;
                cout<<"Erro sintatico: funcao Comando sem Rotulo if, espera-se 'then'\n";
                return nullptr;
            }
            
        }
        delete noComandoSemRotulo; // Este delete é para o caso de noExpressao falhar
        pos = checkpoint;
        cout<<"Erro sintatico: funcao Comando sem Rotulo if, erro na expressão da condicao.\n";
        return nullptr;

    } else if (atual().lexema == "while") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));
        NoSintatico* cond = expressao();
        if (cond && atual().lexema == "do") {
            noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));
            NoSintatico* cmdSemExpr = comandoSemRotulo();
            if (cmdSemExpr) {
                noComandoSemRotulo->filhos.push_back(cmdSemExpr);
                return noComandoSemRotulo;
            }
        }
        pos = checkpoint;
    } else if (atual().lexema == "begin") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));
        
        NoSintatico* noComando = comando();
        if(!noComando){
            delete noComandoSemRotulo;
            pos = checkpoint;
            cout<<"Erro sintatico: funcao Comando sem Rotulo begin, erro ao executar comando()\n";
            return nullptr;
        }
        noComandoSemRotulo->filhos.push_back(noComando);
        while(atual().lexema == ";"){
            noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", ";"));
            NoSintatico* noComando2 = comando();
            if(!noComando2){
                delete noComandoSemRotulo;
                pos = checkpoint;
                cout<<"Erro sintatico: funcao Comando sem Rotulo begin, erro ao executar comando() apos ;\n";
                return nullptr;
            }
            noComandoSemRotulo->filhos.push_back(noComando2);
        }

        if(atual().lexema == "end"){
            noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));
            return noComandoSemRotulo;
        }
        delete noComandoSemRotulo;
        pos = checkpoint;
        cout<<"Erro sintatico: funcao Comando sem Rotulo begin, espera-se end apos execução de comando()\n";
        return nullptr;

    } else if (atual().lexema == "goto") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));

        NoSintatico* num = terminal("Numero");
        if(num){
            noComandoSemRotulo->filhos.push_back(num);
            return noComandoSemRotulo;
        }
        pos = checkpoint;

    //bloco adicionado para write/read que não existia no diagrama, logo não funcionaria em um teste de pascal real
    } else if (atual().lexema == "write" || atual().lexema == "read") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));

        if (!terminal("Simbolo Simples", "(")) {
            delete noComandoSemRotulo;
            cout << "Erro sintatico: espera-se '(' apos '" << tokens[pos-1].lexema << "'\n";
            return nullptr;
        }
        noComandoSemRotulo->filhos.push_back(new NoSintatico("Simbolo Simples", "("));

        //processar a lista de parâmetros (expressões)
        NoSintatico* exprNode = expressao();
        if (!exprNode) {
            delete noComandoSemRotulo;
            cout << "Erro sintatico: expressao invalida dentro de '" << tokens[pos-2].lexema << "'\n";
            return nullptr;
        }
        noComandoSemRotulo->filhos.push_back(exprNode);

        while (atual().lexema == ",") {
            noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", ","));
            exprNode = expressao();
            if (!exprNode) {
                delete noComandoSemRotulo;
                cout << "Erro sintatico: expressao invalida apos a virgula em '" << tokens[pos-3].lexema << "'\n";
                return nullptr;
            }
            noComandoSemRotulo->filhos.push_back(exprNode);
        }
        if (!terminal("Simbolo Simples", ")")) {
            delete noComandoSemRotulo;
            cout << "Erro sintatico: espera-se ')' para fechar a chamada de '" << tokens[pos-1].lexema << "'\n";
            return nullptr;
        }
        noComandoSemRotulo->filhos.push_back(new NoSintatico("Simbolo Simples", ")"));
        return noComandoSemRotulo;

    } else if (atual().lexema == "end" || atual().lexema == ";" || atual().lexema == "else" || atual().tipo == "EOF") {
        return new NoSintatico("ComandoVazio");
    }
    cout<<"Erro sintatico: funcao Comando sem Rotulo, espera-se id/goto/begin/if/while\n";
    return nullptr;
}

NoSintatico* expressao() {
    NoSintatico* esq = expressaoSimples();
    if (!esq) return nullptr;
    string op = atual().lexema;
    if (op == "=" || op == "<" || op == ">" || op == "<=" || op == ">=" || op == "<>") {
        avancar();
        NoSintatico* dir = expressaoSimples();
        if (dir) {
            NoSintatico* no = new NoSintatico("OperacaoRelacional", op);
            no->filhos.push_back(esq);
            no->filhos.push_back(dir);
            return no;
        }
        delete esq;
    }
    return esq;
}

NoSintatico* expressaoSimples() {
    NoSintatico* esq = termo();
    if (!esq) return nullptr;
    while (atual().lexema == "+" || atual().lexema == "-" || atual().lexema == "or") {
        string op = atual().lexema;
        avancar();
        NoSintatico* dir = termo();
        if (dir) {
            NoSintatico* no = new NoSintatico("OperacaoAditiva", op);
            no->filhos.push_back(esq);
            no->filhos.push_back(dir);
            esq = no;
        } else { 
            delete esq; 
            return nullptr; 
        }
    }
    return esq;
}

NoSintatico* termo() {
    NoSintatico* esq = fator();
    if (!esq) return nullptr;
    while (atual().lexema == "*" || atual().lexema == "div" || atual().lexema == "and") {
        string op = atual().lexema;
        avancar();
        NoSintatico* dir = fator();
        if (dir) {
            NoSintatico* no = new NoSintatico("OperacaoMultiplicativa", op);
            no->filhos.push_back(esq);
            no->filhos.push_back(dir);
            esq = no;
        } else { 
            delete esq; 
            return nullptr; 
        }
    }
    return esq;
}

NoSintatico* fator() {
    NoSintatico* noFator = new NoSintatico("fator");

    if (atual().tipo == "Identificador"){
        noFator->filhos.push_back(terminal("Identificador"));

        if(atual().lexema == "["){
            noFator->filhos.push_back(terminal("Simbolo Simples", "["));

            NoSintatico* Exp = expressao();
            if(!Exp){
                delete noFator;
                cout<<"Erro sintatico: funcao Fator id, erro ao executar expressao() apos [\n";
                return nullptr;
            }
            noFator->filhos.push_back(Exp);

            while(atual().lexema == ","){
                noFator->filhos.push_back(terminal("Simbolo Simples", ","));
                
                Exp = expressao();
                if(!Exp){
                    delete noFator;
                    cout<<"Erro sintatico: funcao Fator id, erro ao executar expressao() apos [\n";
                    return nullptr;
                }
                noFator->filhos.push_back(Exp);
            }

            if(atual().lexema == "]"){
                noFator->filhos.push_back(terminal("Simbolo Simples", "]"));
                return noFator;
            }

            delete noFator;
            cout<<"Erro sintatico: funcao Fator id, espera-se ]\n";
            return nullptr;
        }

        if(atual().lexema == "("){
            noFator->filhos.push_back(terminal("Simbolo Simples", "("));

            NoSintatico* expr = expressao();
            if(!expr){
                delete noFator;
                cout<<"Erro sintatico: funcao Fator id, erro ao executar expressao()\n";
                return nullptr;
            }
            noFator->filhos.push_back(expr);

            while (atual().lexema == ",") {
                noFator->filhos.push_back(terminal("Simbolo Simples", ","));

                NoSintatico* exprRep = expressao();
                if (exprRep != nullptr) {
                    noFator->filhos.push_back(exprRep);
                } else {
                    delete noFator;
                    cout<<"Erro sintatico: funcao Fator id, erro ao executar repeticao de expressao()\n";
                    return nullptr;
                }
            }

            if (atual().lexema == ")") {
                noFator->filhos.push_back(terminal("Simbolo Simples", ")"));
                return noFator;
            }
            delete noFator;
            cout<<"Erro sintatico: funcao Fator id, espera-se )\n";
            return nullptr;
        }
        return noFator;
    }
    if (atual().tipo == "Numero"){
        noFator->filhos.push_back(terminal("Numero"));
        return noFator;
    } 

    if (atual().lexema == "(") {
        noFator->filhos.push_back(terminal("Simbolo Simples", "("));

        NoSintatico* exp = expressao();
        if(!exp){
            delete noFator;
            cout<<"Erro sintatico: funcao Fator (, erro ao executar expressao()\n";
            return nullptr;
        }
        noFator->filhos.push_back(exp);

        if (atual().lexema == ")"){
            noFator->filhos.push_back(terminal("Simbolo Simples", ")"));
            return noFator;
        }
        
        delete noFator;
        cout<<"Erro sintatico: funcao Fator (, espera-se )\n";
    }

    if(atual().lexema == "not"){
        noFator->filhos.push_back(terminal("Palavra Reservada"));

        NoSintatico* fatorRec = fator();
        if(!fatorRec){
            delete noFator;
            cout<<"Erro sintatico: funcao Fator not, erro ao executar recursao\n";
            return nullptr;
        }
        noFator->filhos.push_back(fatorRec);
        return noFator;
    }

    delete noFator;
    cout<<"Erro sintatico: funcao Fator deve-se inciar com id/numero/(/not\n";
    return nullptr;
}

// --- Impressão da Arvore ---
void imprimirArvore(NoSintatico* no, int nivel = 0){
    if (!no) return;
    for (int i = 0; i < nivel; i++) cout << "  ";
    cout << no->tipo;
    if (!no->valor.empty()) cout << " (" << no->valor << ")";
    cout << endl;
    for (auto filho : no->filhos) {
        imprimirArvore(filho, nivel + 1);
    }
}

int main() {
    int resultado = criarTabela(); //analisador léxico
    if(resultado != 0) {
        return resultado;
    }

    pos = 0;
    NoSintatico* arvore = programa(); //analisador sintático

    if (arvore && pos >= tokens.size()){
        cout << "Analise sintatica concluida com sucesso!\n\n";
        cout << "--- Arvore Sintatica ---\n";
        imprimirArvore(arvore);
    } else {
        cout << "Erro na analise sintatica!\n";
        if (pos < tokens.size()) {
           cout << "Parou no token " << pos << ": '" << atual().lexema << "' (Linha " << atual().linha << ")\n";
        }
    }
    delete arvore;
    return 0;
}