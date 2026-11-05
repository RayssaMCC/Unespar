#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>
#include <cctype>
#include <unordered_set>
#include <unordered_map>
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
    int linha;
    vector<NoSintatico*> filhos;
    NoSintatico(string tipo, string valor = "", int linha = 0) : tipo(tipo), valor(valor), linha(linha) {}
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

bool isPalavraReservada(const string& palavra) {
    return palavrasReservadas.count(palavra) > 0;
}

bool isSimboloSimples(char c) {
    static const unordered_set<char> simbolos = {'^', '*', '=', '.', ';', ',', '[', ']', '(', ')'};
    return simbolos.count(c) > 0;
}

void analisar(string& codigo) {
    size_t i = 0;
    int linha = 1;

    while(i < codigo.length()) {
        char c = codigo[i];

        if(c == '/' && i+1 < codigo.length() && codigo[i+1] == '/') {
            i += 2;
            while(i < codigo.length() && codigo[i] != '\n') i++;
            continue;
        }

        if(c == '(' && i+1 < codigo.length() && codigo[i+1] == '*') {
            i += 2;
            while(i+1 < codigo.length() && !(codigo[i] == '*' && codigo[i+1] == ')')) {
                if(codigo[i] == '\n') linha++;
                i++;
            }
            if(i+1 < codigo.length()) i += 2;
            continue;
        }

        if(c == '{') {
            i++;
            while(i < codigo.length() && codigo[i] != '}') {
                if(codigo[i] == '\n') linha++;
                i++;
            }
            if(i < codigo.length()) i++;
            continue;
        }

        if(c == '\n') {
            linha++;
            i++;
            continue;
        }

        if(isspace(c) && c != '\n') {
            i++;
            continue;
        }

        if (isalpha(c)) {
            string lexema;
            lexema += c;
            i++;
            while (i < codigo.length() && isalnum(codigo[i])) {
                lexema += codigo[i++];
            }
            string tipo = isPalavraReservada(lexema) ? "Palavra Reservada" : "Identificador";
            tokens.push_back({lexema, tipo, linha});
        }
        else if (isdigit(c)) {
            string numero;
            numero += c;
            i++;
            while (i < codigo.length() && isdigit(codigo[i])) {
                numero += codigo[i++];
            }
            if (i < codigo.length() && codigo[i] == '.' && i + 1 < codigo.length() && isdigit(codigo[i + 1])) {
                numero += codigo[i++];
                while (i < codigo.length() && isdigit(codigo[i])) {
                    numero += codigo[i++];
                }
            }
            tokens.push_back({numero, "Numero", linha});
        }
        else if ((c == '<' || c == '>' || c == '+' || c == '-' || c == ':') && i + 1 < codigo.length()) {
            char prox = codigo[i + 1];
            string composto = string(1, c) + prox;
            if (composto == "<=" || composto == "<>" || composto == ">=" || composto == "++" || composto == "--" || composto == ":=") {
                tokens.push_back({composto, "Simbolo Composto", linha});
                i += 2;
            } else {
                tokens.push_back({string(1, c), "Simbolo Simples", linha});
                i++;
            }
        }
        else if (isSimboloSimples(c)) {
            tokens.push_back({string(1, c), "Simbolo Simples", linha});
            i++;
        }
        else {
            cout << "Erro lexico: linha " << linha << " - Caractere invalido '" << c << "'\n";
            i++;
        }
    }
}

int criarTabela(){
    ifstream entrada("entrada.txt");
    ofstream saida("tabela_simbolos.txt");

    if (!entrada.is_open()) {
        cerr << "Erro ao abrir entrada.txt\n";
        return 1;
    }

    if (!saida.is_open()) {
        cerr << "Erro ao criar tabela_simbolos.txt\n";
        return 1;
    }

    stringstream buffer;
    buffer << entrada.rdbuf();
    string codigo = buffer.str();
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
        NoSintatico* no = new NoSintatico(tipo, atual().lexema, atual().linha);
        avancar();
        return no;
    }
    return nullptr;
}

NoSintatico* programa() {
    int linha = atual().linha;
    NoSintatico* noPrograma = new NoSintatico("programa", "", linha);

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
        cout << "Erro sintatico (linha " << atual().linha << "): Esperava um identificador para o nome do programa\n";
        return nullptr;
    }
    noPrograma->filhos.push_back(id);

    NoSintatico* simbSimples = terminal("Simbolo Simples", "(");
    if (simbSimples){
        noPrograma->filhos.push_back(simbSimples);
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
            cout << "Erro sintatico (linha " << atual().linha << "): Esperava ')' para fechar lista de parâmetros do programa.\n";
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
    noPrograma->filhos.push_back(noBloco);

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
    int linha = atual().linha;
    NoSintatico* noBloco = new NoSintatico("Bloco", "", linha);

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
                cout<<"Erro sintatico: funcao Bloco, espera-se um Numero apos a ,\n";
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
                cout<<"Erro sintatico: funcao Bloco var, espera-se um ; apos tipo()\n";
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
                cout<<"Erro sintatico: funcao Bloco procedure/function, tipo de retorno da funcao e invalido.\n";
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
    delete noBloco;
    cout << "Erro sintatico: espera-se 'begin' ou outra estrutura valida no bloco\n";
    return nullptr;
}

NoSintatico* tipo() {
    NoSintatico* noTipo = new NoSintatico("Tipo", "", atual().linha);

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
    else if (atual().tipo == "Palavra Reservada" && (atual().lexema == "integer" || atual().lexema == "boolean" || atual().lexema == "double")) {
        noTipo->filhos.push_back(terminal("Palavra Reservada"));
        return noTipo;
    }
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
    NoSintatico* noParametrosFormais = new NoSintatico("Parametros Formais", "", atual().linha);

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

NoSintatico* comando() {
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
    NoSintatico* noComandoSemRotulo = new NoSintatico("Comando Sem Rotulo", "", atual().linha);

    if (atual().tipo == "Identificador") {
         noComandoSemRotulo->filhos.push_back(terminal("Identificador"));

        if (atual().lexema == ":=" || atual().lexema == "[") {
            if(atual().lexema == "["){
                noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", "["));

                NoSintatico* noExpressao = expressao();
                if(!noExpressao){
                    delete noComandoSemRotulo;
                    pos = checkpoint;
                    cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro na execução da expressao apos [ \n";
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
                cout<<"Erro sintatico: funcao Comando sem Rotulo id, espera-se := apos id "<< atual().lexema << "   " << tokens[pos-1].lexema << "\n";
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
                cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro ao executar expressao() apos (\n";
                return nullptr;
            }
            noComandoSemRotulo->filhos.push_back(noExpressao1);

            while (atual().lexema == ",") { // se houver mais de um parâmetro
                noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", ","));

                NoSintatico* noExpressao2 = expressao();
                if(!noExpressao2) { 
                    delete noComandoSemRotulo;
                    pos = checkpoint; 
                    cout<<"Erro sintatico: funcao Comando sem Rotulo id, erro ao executar expressao() apos ,\n";
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
                delete noComandoSemRotulo;
                pos = checkpoint;
                cout<<"Erro sintatico: funcao Comando sem Rotulo if, espera-se 'then'\n";
                return nullptr;
            }
            
        }
        delete noComandoSemRotulo; //para o caso de noExpressao falhar
        pos = checkpoint;
        cout<<"Erro sintatico: funcao Comando sem Rotulo if, erro na expressao da condicao.\n";
        return nullptr;

    } else if (atual().lexema == "while") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada", "while"));
        
        NoSintatico* cond = expressao();
        if (cond) {
            noComandoSemRotulo->filhos.push_back(cond);
        } else {
            delete noComandoSemRotulo;
            pos = checkpoint;
            cout << "Erro sintatico: expressao invalida na condicao do 'while'\n";
            return nullptr;
        }

        if (atual().lexema == "do") {
            noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada", "do"));
            NoSintatico* cmdSemExpr = comandoSemRotulo();
            if (cmdSemExpr) {
                noComandoSemRotulo->filhos.push_back(cmdSemExpr);
                return noComandoSemRotulo;
            }
        }
        
        delete noComandoSemRotulo;
        pos = checkpoint;
        cout << "Erro sintatico: faltou 'do' ou comando invalido apos 'while'\n";
        return nullptr;
    
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
        cout<<"Erro sintatico: funcao Comando sem Rotulo begin, espera-se end apos execucao de comando()\n";
        return nullptr;

    } else if (atual().lexema == "goto") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));

        NoSintatico* num = terminal("Numero");
        if(num){
            noComandoSemRotulo->filhos.push_back(num);
            return noComandoSemRotulo;
        }
        pos = checkpoint;

    //bloco adicionado para write/read que nao existia no diagrama, logo, nao funcionaria em um teste de pascal real
    } else if (atual().lexema == "write" || atual().lexema == "read") {
        noComandoSemRotulo->filhos.push_back(terminal("Palavra Reservada"));

        if (!terminal("Simbolo Simples", "(")) {
            delete noComandoSemRotulo;
            cout << "Erro sintatico: espera-se '(' apos '" << tokens[pos-1].lexema << "'\n";
            return nullptr;
        }
        noComandoSemRotulo->filhos.push_back(new NoSintatico("Simbolo Simples", "("));

        NoSintatico* exprNo = expressao();
        if (!exprNo) {
            delete noComandoSemRotulo;
            cout << "Erro sintatico: expressao invalida dentro de '" << tokens[pos-2].lexema << "'\n";
            return nullptr;
        }
        noComandoSemRotulo->filhos.push_back(exprNo);

        while (atual().lexema == ",") {
            noComandoSemRotulo->filhos.push_back(terminal("Simbolo Simples", ","));
            exprNo = expressao();
            if (!exprNo) {
                delete noComandoSemRotulo;
                cout << "Erro sintatico: expressao invalida apos a virgula em '" << tokens[pos-3].lexema << "'\n";
                return nullptr;
            }
            noComandoSemRotulo->filhos.push_back(exprNo);
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
    NoSintatico* noFator = new NoSintatico("fator", "", atual().linha);

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
            cout<<"Erro sintatico: funcao Fator '(', erro ao executar expressao()\n";
            return nullptr;
        }
        noFator->filhos.push_back(exp);

        if (atual().lexema == ")"){
            noFator->filhos.push_back(terminal("Simbolo Simples", ")"));
            return noFator;
        }

        delete noFator;
        cout<<"Erro sintatico: funcao Fator '(', espera-se )\n";
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

struct Simbolo{
    string nome;
    string tipo;
    string categoria;
    Simbolo(string n = "", string t = "", string cat = ""): nome(n), tipo(t), categoria(cat){}
};

class TabelaSimb{
private:
    vector<unordered_map<string, Simbolo>> pilhaEscopo;
public:
    TabelaSimb(){
        criarEscopo();
    }

    void criarEscopo(){
        pilhaEscopo.push_back(unordered_map<string, Simbolo>());
    }

    void sairEscopo(){
        if(!pilhaEscopo.empty()){
            pilhaEscopo.pop_back();
        }
    }

    bool incerirSimb(const Simbolo& simb){
        if(pilhaEscopo.empty()){
            return false;
        }
        if(pilhaEscopo.back().count(simb.nome)){
            return false;
        }
        pilhaEscopo.back()[simb.nome] = simb;
        return true;
    }

    Simbolo* buscarSimb(const string& simbNome){
        for(auto i = pilhaEscopo.rbegin(); i != pilhaEscopo.rend(); i++){
            if(i->count(simbNome)){
                return &((*i)[simbNome]);
            }
        }
        return nullptr;
    }
};

class AnalisadorSemantico{
private:
    TabelaSimb tabela;
    bool houveErro;

    void erro(int linha, const string& mensagem){
        cout << "Erro semantico (linha " << linha << "): " << mensagem << "\n";
        houveErro = true;
    }
    void visitar(NoSintatico* no);
    void visitarBloco(NoSintatico* no);
    void visitarAtribuicao(NoSintatico* no);
    string avaliarTipoExpressao(NoSintatico* no);

public:
    AnalisadorSemantico(){
        houveErro = false;
    }

    bool analisar(NoSintatico* raiz){
        visitar(raiz);
        return !houveErro;
    }
};

void AnalisadorSemantico::visitar(NoSintatico* arvSintatica){
    if(!arvSintatica){
        return;
    }

    string tipoNo = arvSintatica->tipo;

    if(tipoNo == "programa"){
        for(auto filho : arvSintatica->filhos){
            if(filho->tipo == "Bloco"){
                visitar(filho);
                break;
            }
        }
    }else if(tipoNo == "Bloco"){
        visitarBloco(arvSintatica);
    }else if(tipoNo == "Comando Sem Rotulo"){
        if(!arvSintatica->filhos.empty() && arvSintatica->filhos[0]->tipo == "Identificador"){
            if(arvSintatica->filhos.size() > 1 && arvSintatica->filhos[1]->valor == ":="){
                visitarAtribuicao(arvSintatica);
            }
        }else if(!arvSintatica->filhos.empty() && arvSintatica->filhos[0]->valor == "if"){
            NoSintatico* exprNo = arvSintatica->filhos[1];
            string tipoExpr = avaliarTipoExpressao(exprNo);
            if(tipoExpr != "boolean"){
                erro(exprNo->linha, "Expressao do 'if' deve ser booleana, mas encontrou '" + tipoExpr + "'");
            }
            for(size_t i = 2; i < arvSintatica->filhos.size(); i++){
                visitar(arvSintatica->filhos[i]);
            }
        }else if(!arvSintatica->filhos.empty() && arvSintatica->filhos[0]->valor == "while"){
            NoSintatico* exprNo = arvSintatica->filhos[1];
            string tipoExpr = avaliarTipoExpressao(exprNo);
            if(tipoExpr != "boolean"){
                erro(exprNo->linha, "Expressao do 'while' deve ser booleana, mas encontrou '" + tipoExpr + "'");
            }
            for(size_t i = 2; i < arvSintatica->filhos.size(); i++){
                visitar(arvSintatica->filhos[i]);
            }
        }else{
            for(auto filho : arvSintatica->filhos){
                visitar(filho);
            }
        }
    }else if(tipoNo == "OperacaoRelacional" || tipoNo == "OperacaoAditiva" || tipoNo == "OperacaoMultiplicativa"){
        avaliarTipoExpressao(arvSintatica);
    }else{
        for(auto filho : arvSintatica->filhos){
            visitar(filho);
        }
    }
}

void AnalisadorSemantico::visitarBloco(NoSintatico* noBloco){
    tabela.criarEscopo();
    size_t interador = 0;
    while(interador < noBloco->filhos.size() && noBloco->filhos[interador]->valor != "begin"){
        NoSintatico* marcador = noBloco->filhos[interador];

        if(marcador->valor == "type"){
            interador++;
            while(interador < noBloco->filhos.size() && noBloco->filhos[interador]->tipo == "Identificador"){
                string id = noBloco->filhos[interador]->valor;
                interador += 2;

                NoSintatico* noTipo = noBloco->filhos[interador];
                string nomeTipo;
                for(auto filho : noTipo->filhos){
                    if(filho->tipo == "Identificador" || filho->valor == "integer" || filho->valor == "boolean" || filho->valor == "double"){
                        nomeTipo = filho->valor;
                        interador++;
                        break;
                    }
                }

                Simbolo simb(id, nomeTipo, "tipo");
                if(!tabela.incerirSimb(simb)){
                    erro(noBloco->filhos[interador-2]->linha, "Tipo '" + simb.nome + "' ja declarado neste escopo");
                    goto fim_bloco;
                }
                interador++;
            }
        }
        else if(marcador->valor == "var"){
            interador++;
            while(interador < noBloco->filhos.size() && noBloco->filhos[interador]->tipo == "Identificador"){
                vector<NoSintatico*> ids;
                while(interador < noBloco->filhos.size() && noBloco->filhos[interador]->tipo == "Identificador"){
                    ids.push_back(noBloco->filhos[interador]);
                    interador++;
                    if(interador < noBloco->filhos.size() && noBloco->filhos[interador]->valor == ","){
                        interador++;
                    }else{
                        break;
                    }
                }

                interador++;

                NoSintatico* noTipo = noBloco->filhos[interador];
                string nomeTipo;
                for(auto filho : noTipo->filhos){
                    if(filho->tipo == "Identificador" || filho->valor == "integer" || filho->valor == "boolean" || filho->valor == "double"){
                        nomeTipo = filho->valor;
                        interador++;
                        break;
                    }
                    if(filho->valor == "array"){
                        nomeTipo = "array of ";
                        for(size_t i = 0; i < filho->filhos.size(); i++){
                            if(filho->filhos[i]->valor == "of"){
                                nomeTipo += filho->filhos[i+1]->filhos[0]->valor;
                                interador++;
                                break;
                            }
                        }
                        break;
                    }
                }

                for(auto noId : ids){
                    Simbolo simb(noId->valor, nomeTipo, "variavel");
                    if(!tabela.incerirSimb(simb)){
                        erro(noId->linha, "Variavel '" + simb.nome + "' ja declarada neste escopo");
                        goto fim_bloco;
                    }
                }
                interador++;
            }
        }
        else if(marcador->valor == "function" || marcador->valor == "procedure"){
            interador += 2;//consome a palavra reservada e o id
            if(noBloco->filhos[interador]->tipo == "Parametro Formais"){
                NoSintatico* parametroFormal = noBloco->filhos[interador];
                interador++; //consome  parametros formais de bloco
                size_t i = 0; //interador de parametros formais

                do{
                    if(parametroFormal->filhos[i]->valor == "var" || parametroFormal->filhos[i-1]->valor != "procedure"){
                        i++;
                    } 
                    if(parametroFormal->filhos[i]->tipo == "Identificador" && (parametroFormal->filhos[i-1]->valor != "function" && parametroFormal->filhos[i-1]->valor != "procedure")){
                        while(i < parametroFormal->filhos.size() && parametroFormal->filhos[i]->tipo == "Identificador"){
                            vector<NoSintatico*> ids;
                            while(i < parametroFormal->filhos.size() && parametroFormal->filhos[i]->tipo == "Identificador"){
                                ids.push_back(parametroFormal->filhos[i]);
                                i++;
                                if(i < parametroFormal->filhos.size() && parametroFormal->filhos[i]->valor == ","){
                                    i++;
                                }else{
                                    break;
                                }
                            }
                            i++; // consome os :

                            string nomeTipo;
                            if(parametroFormal->filhos[i]->tipo == "Identificador" || parametroFormal->filhos[i]->valor == "integer" || parametroFormal->filhos[i]->valor == "boolean" || parametroFormal->filhos[i]->valor == "double"){
                                nomeTipo = parametroFormal->filhos[i]->valor;
                                i++;
                            }

                            for(auto noId : ids){
                                Simbolo simb(noId->valor, nomeTipo, "variavel");
                                if(!tabela.incerirSimb(simb)){
                                    erro(noId->linha, "Variavel '" + simb.nome + "' ja declarada neste escopo");
                                    goto fim_bloco;
                                }
                            }
                            i++; // consome )
                        }
                    }else{
                        if(parametroFormal->filhos[i]->valor == "procedure"){
                            while(parametroFormal->filhos[i]->valor != ";"){
                                i++;
                            }
                        }
                    }
                }while(parametroFormal->filhos[i]->valor != ")");
            }
            
            if(noBloco->filhos[interador]->valor == ":"){
                interador++; // consome :
                Simbolo* id = tabela.buscarSimb(noBloco->filhos[interador]->valor); // o proximo é um id
                if(!id){
                    erro(noBloco->filhos[interador]->linha, "Variavel '" + noBloco->filhos[interador]->valor + "' nao declarada");
                    return;
                }
                if(id->categoria != "variavel"){
                    erro(noBloco->filhos[interador]->linha, "Identificador '" + noBloco->filhos[interador]->valor + "' nao eh uma variavel");
                    return;
                }
                interador++; // consome id
            }
            interador++;  // Consome ;
            visitarBloco(noBloco->filhos[interador]); // novo escopo
            interador++;  // consome ;
        }else{
            interador ++;
        }
    }

    while(interador < noBloco->filhos.size()){
        NoSintatico* noAtual = noBloco->filhos[interador];
        if(noAtual->valor == "begin" || noAtual->valor == "end" || noAtual->valor == ";"){
            interador++;
            continue;
        }
        visitar(noAtual);
        interador++;
    }
fim_bloco:
    tabela.sairEscopo();
}

void AnalisadorSemantico::visitarAtribuicao(NoSintatico* noAtribuicao){
    NoSintatico* varNo = noAtribuicao->filhos[0];
    Simbolo* simbolo = tabela.buscarSimb(varNo->valor);

    if(!simbolo){
        erro(varNo->linha, "Variavel '" + varNo->valor + "' nao declarada");
        return;
    }
    if(simbolo->categoria != "variavel"){
        erro(varNo->linha, "Identificador '" + varNo->valor + "' nao eh uma variavel");
        return;
    }
    NoSintatico* expressaoNo = noAtribuicao->filhos.back();
    string tipoExpressao = avaliarTipoExpressao(expressaoNo);

    if(tipoExpressao != "ERRO" && simbolo->tipo != tipoExpressao){
        erro(expressaoNo->linha, "Tipo incompativel para atribuicao: esperado '" + simbolo->tipo + "', mas encontrado '" + tipoExpressao + "'");
    }
}

string AnalisadorSemantico::avaliarTipoExpressao(NoSintatico* no){
    if(!no){
        return "ERRO";
    }

    if(no->tipo == "Numero"){
        return (no->valor.find('.') != string::npos) ? "double" : "integer";
    }
    if(no->tipo == "Identificador"){
        Simbolo* simb = tabela.buscarSimb(no->valor);
        if(!simb){
            erro(no->linha, "Variavel ou funcao '" + no->valor + "' nao declarada");
            return "ERRO";
        }
        return simb->tipo;
    }
    if(no->tipo == "fator"){
        if(no->filhos.size() == 1){
            return avaliarTipoExpressao(no->filhos[0]);
        }
        // Se o fator for uma expressão entre parênteses: fator -> ( expressao )
        if (!no->filhos.empty() && no->filhos[0]->valor == "(") {
            return avaliarTipoExpressao(no->filhos[1]); // Avalia o que tem dentro dos parênteses
        }
        // Se o fator for simples (ex: um número), ele terá um filho (o próprio número)
        if (no->filhos.size() == 1) {
            return avaliarTipoExpressao(no->filhos[0]);
        }
        // Caso: fator -> not fator
        if (no->filhos[0]->valor == "not") {
            string tipoFator = avaliarTipoExpressao(no->filhos[1]);
            if (tipoFator != "boolean") {
                erro(no->linha, "O operador 'not' exige um operando booleano, mas encontrou '" + tipoFator + "'");
                return "ERRO";
            }
            return "boolean";
        }
        if(no->filhos[0]->tipo == "Identificador" && no->filhos.size() > 1 && no->filhos[1]->valor == "["){
            Simbolo* simb = tabela.buscarSimb(no->filhos[0]->valor);
            if(!simb){
                erro(no->filhos[0]->linha, "Variavel '" + no->filhos[0]->valor + "' nao declarada");
                return "ERRO";
            }
            if(simb->tipo.find("array") == 0){
                for(size_t i = 2; i < no->filhos.size() && no->filhos[i]->valor != "]"; i += 2){
                    string tipoIdx = avaliarTipoExpressao(no->filhos[i]);
                    if(tipoIdx != "integer"){
                        erro(no->filhos[i]->linha, "Indice de array deve ser inteiro, mas encontrou '" + tipoIdx + "'");
                        return "ERRO";
                    }
                }
                string tipoBase = simb->tipo.substr(simb->tipo.find("of") + 3);
                return tipoBase;
            }
            erro(no->filhos[0]->linha, "Identificador '" + no->filhos[0]->valor + "' nao eh um array");
            return "ERRO";
        }
        if(no->filhos[0]->tipo == "Identificador" && no->filhos.size() > 1 && no->filhos[1]->valor == "("){
            Simbolo* simb = tabela.buscarSimb(no->filhos[0]->valor);
            if(!simb){
                erro(no->filhos[0]->linha, "Funcao ou procedimento '" + no->filhos[0]->valor + "' nao declarado");
                return "ERRO";
            }
            if(simb->categoria != "function" && simb->categoria != "procedure"){
                erro(no->filhos[0]->linha, "Identificador '" + no->filhos[0]->valor + "' nao eh uma funcao ou procedimento");
                return "ERRO";
            }
            return simb->tipo;
        }
    }
    if(no->tipo == "termo" || no->tipo == "expressaoSimples"){
        if(no->filhos.size() == 1){
            return avaliarTipoExpressao(no->filhos[0]);
        }
        erro(no->linha, "No '" + no->tipo + "' com numero invalido de filhos: " + to_string(no->filhos.size()));
        return "ERRO";
    }
    if(no->tipo == "OperacaoAditiva" || no->tipo == "OperacaoMultiplicativa"){
        string tipoEsq = avaliarTipoExpressao(no->filhos[0]);
        string tipoDir = avaliarTipoExpressao(no->filhos[1]);
        string operando = no->valor;

        // Se um dos lados já deu erro, nao continua
        if (tipoEsq == "ERRO" || tipoDir == "ERRO") {
            return "ERRO";
        }

        if(operando == "or" || operando == "and"){
            if(tipoEsq != "boolean" || tipoDir != "boolean"){
                erro(no->linha, "Operacao '" + operando + "' exige operandos booleanos, mas encontrou '" + tipoEsq + "' e '" + tipoDir + "'");
                return "ERRO";
            }
            return "boolean";
        }

        if((tipoEsq == "integer" || tipoEsq == "double") && (tipoDir == "integer" || tipoDir == "double")){
            if(tipoEsq == "double" || tipoDir == "double"){
                return "double";
            }
            return "integer";
        }

        erro(no->linha, "Tipos incompativeis para operacao '" + operando + "': '" + tipoEsq + "' e '" + tipoDir + "'");
        return "ERRO";
    }
    if(no->tipo == "OperacaoRelacional"){
        string tipoEsq = avaliarTipoExpressao(no->filhos[0]);
        string tipoDir = avaliarTipoExpressao(no->filhos[1]);
        if(tipoEsq == "ERRO" || tipoDir == "ERRO"){
            return "ERRO";
        }
        bool compativel = (tipoEsq == tipoDir);
        if(!compativel){
            erro(no->linha, "Tipos incompativeis para operacao relacional '" + no->valor + "': '" + tipoEsq + "' e '" + tipoDir + "'");
            return "ERRO";
        }
        return "boolean";
    }

    if(!no->filhos.empty()){
        return avaliarTipoExpressao(no->filhos[0]);
    }
    erro(no->linha, "No '" + no->tipo + "' nao suportado ou invalido");
    return "ERRO";
}

void imprimirArvore(NoSintatico* no, int nivel = 0) {
    if (!no) return;
    for (int i = 0; i < nivel; ++i) cout << "  ";
    cout << no->tipo;
    if (!no->valor.empty()) cout << " (" << no->valor << ")";
    cout << " [Linha " << no->linha << "]\n";
    for (auto filho : no->filhos) {
        imprimirArvore(filho, nivel + 1);
    }
}

int main() {
    int resultadoLexico = criarTabela(); //analisador léxico
    if (resultadoLexico != 0) {
        return resultadoLexico;
    }
    cout << "\nIniciando analise sintatica...\n";
    pos = 0;
    NoSintatico* arvore = programa(); //analisador sintático
    if (arvore && pos >= (int)tokens.size()) {
        cout << "Analise sintatica concluida com sucesso!\n\n";
        cout << "--- Arvore Sintatica ---\n";
        imprimirArvore(arvore);
        cout << "------------------------\n\n";
        cout << "Iniciando analise semantica...\n";
        AnalisadorSemantico analisadorSemantico;
        bool sucessoSemantico = analisadorSemantico.analisar(arvore); //analisador semântico
        if (sucessoSemantico) {
            cout << "Analise semantica concluida com sucesso! Nenhum erro encontrado.\n";
        } else {
            cout << "Analise semantica concluida com erros.\n";
        }
    } else {
        cout << "\nErro na analise sintatica!\n";
        if (pos < (int)tokens.size()) {
            cout << "Parou no token " << pos << ": '" << atual().lexema << "' (Linha " << atual().linha << ")\n";
        } else {
            cout << "Erro inesperado no final da entrada.\n";
        }
    }
    delete arvore;
    return 0;
}