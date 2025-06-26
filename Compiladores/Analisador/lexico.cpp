//Analisador léxico - Marielly e Rayssa

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cctype>
#include <iomanip> // Para formatação da saída
#include <unordered_set> // Mais rápido que vector para busca e ignora duplicatas
using namespace std;

struct Token {
    string lexema;
    string tipo;
    int linha;
};

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

vector<Token> analisar(string& codigo) {
    vector<Token> tokens; // vetor que armazena os tokens encontrados
    size_t i = 0; //codigo.length retorna um size_t, então pra comparar é melhor usar o mesmo tipo
    int linha = 1;

    while (i < codigo.length()) {

        char c = codigo[i];

        //ignora comentários de linha //
        if (codigo[i] == '/' && i + 1 < codigo.length() && codigo[i + 1] == '/') {
            i += 2; // pula os dois caracteres: //
            while (i < codigo.length() && codigo[i] != '\n') {
                i++;
            }
            continue;
        }

        //ignora comentários de bloco (* *)
        if (codigo[i] == '(' && i + 1 < codigo.length() && codigo[i + 1] == '*') {
            i += 2; // pula os dois caracteres: (*
            while (i + 1 < codigo.length() && !(codigo[i] == '*' && codigo[i + 1] == ')')) {
                if (codigo[i] == '\n') linha++;
                i++;
            }
            if (i + 1 < codigo.length()) i += 2; // pula o *)
            continue;
        }

        //ignora comentários de bloco { }
        if(c == '{'){
           while (i + 1 < codigo.length() && codigo[i] != '}') {
                if (codigo[i] == '\n') linha++;
                i++;
            }
            if (i + 1 < codigo.length()) i++; // pula o }
            continue;
        }

        if (codigo[i] == '\n') { // Atualiza contador de linhas

            linha++; 
            i++; 
            continue; 
        } 
        if (isspace(codigo[i]) && c != '\n') { // Ignora espaços em branco
            i++;  
            continue; 
        }

        // E1 → E2 (Identificador ou palavra reservada)
        if (isalpha(c)) {
            string lexema;
            lexema += c;
            i++;

            // E2 → E2 (letras e números)
            while (i < codigo.length() && isalnum(codigo[i])) {
                lexema += codigo[i++];
            }

            // Verifica se é palavra reservada ou identificador
            string tipo = isPalavraReservada(lexema) ? "Palavra Reservada" : "Identificador";
            tokens.push_back({lexema, tipo, linha});

        }else if (isdigit(c)) { // E1 → E3 → E4 (Número inteiro ou real)
            string numero;
            numero += c;
            i++;

            while (i < codigo.length() && isdigit(codigo[i])) {
                numero += codigo[i++];
            }

            // Verifica se é número com ponto decimal
            if (i < codigo.length() && codigo[i] == '.' && i + 1 < codigo.length() && isdigit(codigo[i + 1])) {
                numero += codigo[i++]; // adiciona ponto
                while (i < codigo.length() && isdigit(codigo[i])) {
                    numero += codigo[i++];
                }
            }

            tokens.push_back({numero, "Número", linha});
        }

        // E1 → E7/E9/E11/E13/E15 → E8/E10/E12/E14/E16 (Símbolos compostos)
        else if ((c == '<' || c == '>' || c == '+' || c == '-' || c == ':') && i + 1 < codigo.length()) {
            char prox = codigo[i + 1];
            string composto = string(1, c) + prox; //string de 1 caractere com o valor de c + o próximo caractere

            if (composto == "<=" || composto == "<>" || composto == ">=" || composto == "++" || composto == "--" || composto == ":=") {
                tokens.push_back({composto, "Símbolo Composto", linha});
                i += 2; // avança 2 posições pois já processou os dois caracteres
            } else {
                tokens.push_back({string(1, c), "Símbolo Simples", linha});  // E7/E9/E11/E13/E15 (apenas símbolos simples que iniciam um composto)
                i++;
            }
        }

        // E1 → E6 (Símbolos simples: ^ * = . ; , ( ) [ ] )
        else if (isSimboloSimples(c)) {
            tokens.push_back({string(1, c), "Símbolo Simples", linha});
            i++;
        }

        // E1 → ? (Erro léxico)
        else {
            cout << "Erro lexico: linha " << linha << " - Caractere invalido '" << c << "'\n";
            i++;
        }
    }

    return tokens;
}

int main() {
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

    vector<Token> tokens = analisar(codigo);

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