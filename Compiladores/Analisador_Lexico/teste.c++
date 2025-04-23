// Analisador léxico para Pascal Simplificado
// Linguagem: C++
// Entrada: Arquivo .txt com código Pascal
// Saída: Arquivo .txt com tabela de símbolos (lexema e tipo)

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <cctype>

using namespace std;

// Palavras reservadas da linguagem
unordered_set<string> palavras_reservadas = {
    "program", "read", "write", "integer", "boolean", "double", "function",
    "procedure", "begin", "end", "and", "array", "case", "const", "div",
    "do", "downto", "else", "file", "for", "goto", "if", "in", "label",
    "mod", "nil", "not", "of", "or", "packed", "record", "repeat", "set",
    "then", "to", "type", "until", "with", "var", "while"
};

// Símbolos simples
unordered_set<char> simbolos_simples = {
    '[', ']', '{', '}', ':', ';', '.', ',', '+', '-', '<', '>', '=', '^', '*'
};

// Símbolos compostos
unordered_set<string> simbolos_compostos = {
    "<>", "<=", ">=", "++", "--", ":="
};

// Estrutura da tabela de símbolos
struct Simbolo {
    string lexema;
    string tipo;
};

// Verifica se um caractere é válido em um identificador
bool caractere_valido_identificador(char c) {
    return isalnum(c) || c == '_';
}

// Função principal de análise léxica
vector<Simbolo> analisador_lexico(const string& codigo) {
    vector<Simbolo> tabela;
    int i = 0;
    while (i < codigo.size()) {
        // Ignora espaços e quebras de linha
        if (isspace(codigo[i])) {
            i++;
            continue;
        }

        // Verifica identificadores ou palavras reservadas
        if (isalpha(codigo[i])) {
            string lexema;
            while (i < codigo.size() && caractere_valido_identificador(codigo[i])) {
                lexema += tolower(codigo[i]);
                i++;
            }
            if (palavras_reservadas.count(lexema)) {
                tabela.push_back({lexema, "palavra_reservada"});
            } else if (isdigit(lexema[0])) {
                tabela.push_back({lexema, "erro_lexico"}); // identificador inválido
            } else {
                tabela.push_back({lexema, "identificador"});
            }
        }
        // Verifica números inteiros
        else if (isdigit(codigo[i])) {
            string numero;
            while (i < codigo.size() && isdigit(codigo[i])) {
                numero += codigo[i];
                i++;
            }
            tabela.push_back({numero, "numero"});
        }
        // Verifica símbolos compostos (dois caracteres)
        else if (i + 1 < codigo.size()) {
            string dois_chars = string(1, codigo[i]) + codigo[i + 1];
            if (simbolos_compostos.count(dois_chars)) {
                tabela.push_back({dois_chars, "simbolo_composto"});
                i += 2;
                continue;
            }
        }
        // Verifica símbolos simples
        if (simbolos_simples.count(codigo[i])) {
            tabela.push_back({string(1, codigo[i]), "simbolo_simples"});
            i++;
        } else {
            // Qualquer outro caractere é erro léxico
            tabela.push_back({string(1, codigo[i]), "erro_lexico"});
            i++;
        }
    }
    return tabela;
}

int main() {
    ifstream arquivo_entrada("entrada.txt");
    ofstream arquivo_saida("tabela_simbolos.txt");
    
    if (!arquivo_entrada.is_open()) {
        cerr << "Erro ao abrir o arquivo de entrada." << endl;
        return 1;
    }

    stringstream buffer;
    buffer << arquivo_entrada.rdbuf();
    string codigo = buffer.str();

    vector<Simbolo> tabela = analisador_lexico(codigo);

    for (const auto& simbolo : tabela) {
        arquivo_saida << simbolo.lexema << "\t" << simbolo.tipo << endl;
    }

    cout << "Análise léxica concluída. Veja o arquivo 'tabela_simbolos.txt'." << endl;

    return 0;
}
