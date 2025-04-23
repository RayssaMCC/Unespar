import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Memoria {
    int tamanho; //Armazena o tamanho do bloco de memória
    boolean livre; //Indica se o bloco de memória está livre ou ocupado

    public Memoria(int tamanho, boolean livre) {
        this.tamanho = tamanho;
        this.livre = livre;
    }

    @Override
    public String toString() {
        //Retorna uma representação em string do bloco de memória, mostrando seu tamanho e se está livre
        return "(" + tamanho + "," + livre + ")";
    }
}

class GerenciadorDeMemoria {
    List<Memoria> memorias; //Lista para armazenar os blocos de memória

    public GerenciadorDeMemoria(int tamanhoInicial) {
        memorias = new ArrayList<>();
        //Inicializa a lista de memórias com um bloco do tamanho inicial e livre
        memorias.add(new Memoria(tamanhoInicial, true));
    }

    //Política de primeiro ajuste
    public void primeiroAjuste(int tamanho) {
        for (Memoria memoria : memorias) {
            if (memoria.livre && memoria.tamanho >= tamanho) {
                dividirBloco(memoria, tamanho); //Divide o bloco de memória se for livre e grande o suficiente
                return;
            }
        }
        System.out.println("Memoria insuficiente para alocar " + tamanho + " KB");
    }

    //Política de melhor ajuste
    public void melhorAjuste(int tamanho) {
        Memoria melhor = null;
        for (Memoria memoria : memorias) {
            if (memoria.livre && memoria.tamanho >= tamanho) {
                if (melhor == null || memoria.tamanho < melhor.tamanho) {
                    melhor = memoria; //Encontra o bloco livre com o menor tamanho necessário
                }
            }
        }
        if (melhor != null) {
            dividirBloco(melhor, tamanho);
        } else {
            System.out.println("Memoria insuficiente para alocar " + tamanho + " KB");
        }
    }

    //Política de pior ajuste
    public void piorAjuste(int tamanho) {
        Memoria pior = null;
        for (Memoria memoria : memorias) {
            if (memoria.livre && memoria.tamanho >= tamanho) {
                if (pior == null || memoria.tamanho > pior.tamanho) {
                    pior = memoria; //Encontra o maior bloco livre disponível
                }
            }
        }
        if (pior != null) {
            dividirBloco(pior, tamanho);
        } else {
            System.out.println("Memoria insuficiente para alocar " + tamanho + " KB");
        }
    }

    //Divide um bloco de memória, atualizando o tamanho do bloco original e inserindo um novo bloco livre se necessário
    private void dividirBloco(Memoria memoria, int tamanho) {
        if (memoria.tamanho > tamanho) {
            memorias.add(memorias.indexOf(memoria) + 1, new Memoria(memoria.tamanho - tamanho, true)); //Insere um novo bloco livre com o tamanho restante
        }
        memoria.tamanho = tamanho;
        memoria.livre = false; //Atualiza o bloco original para ocupado com o novo tamanho
    }

    //Libera um bloco de memória especificado pelo tamanho
    public void liberarMemoria(int tamanho) {
        for (Memoria memoria : memorias) {
            if (!memoria.livre && memoria.tamanho == tamanho) {
                memoria.livre = true; //Libera o bloco de memória especificado
                fundirBlocosLivres(); //Tenta fundir blocos livres adjacentes
                return;
            }
        }
        System.out.println("Bloco de " + tamanho + " KB nao encontrado.");
    }

    //Funde blocos livres adjacentes para formar um bloco maior
    private void fundirBlocosLivres() {
        for (int i = 0; i < memorias.size() - 1; i++) {
            Memoria atual = memorias.get(i);
            Memoria proximo = memorias.get(i + 1);
            if (atual.livre && proximo.livre) {
                atual.tamanho += proximo.tamanho; //Funde dois blocos livres adjacentes
                memorias.remove(i + 1); //Remove o bloco fundido
                i--; //Ajusta o índice após a remoção
            }
        }
    }

    //Exibe o estado atual da memória
    public void exibirMemoria() {
        for (Memoria memoria : memorias) {
            System.out.print(memoria + " "); //Exibe cada bloco de memória
        }
        System.out.println();
    }
}

public class PoliticaSelecao {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Informe a quantidade total de KB: ");
        int tamanhoInicial = sc.nextInt();
        
        GerenciadorDeMemoria gerenciador = new GerenciadorDeMemoria(tamanhoInicial);

        char politica;

        do {
            System.out.println("\nEscolha a politica de alocacao:");
            System.out.println("1 - Primeiro ajuste");
            System.out.println("M - Melhor ajuste");
            System.out.println("P - Pior ajuste");
            politica = Character.toUpperCase(sc.next().charAt(0)); //Converte a entrada para maiúscula

            if (politica != '1' && politica != 'M' && politica != 'P') {
                System.out.println("Politica invalida!");
            }
        } while (politica != '1' && politica != 'M' && politica != 'P');

        char instrucao;

        do {
            System.out.println("\nEscolha uma opcao:");
            System.out.println("I - Inserir memoria");
            System.out.println("L - Liberar memoria");
            System.out.println("X - Sair");
            instrucao = Character.toUpperCase(sc.next().charAt(0)); //Converte a entrada para maiúscula
            
            //Executa a operação escolhida
            if (instrucao == 'I') { //Insere memória
                System.out.print("\nDigite a quantidade de KB: ");
                int tamanho = sc.nextInt();
                
                //Executa a política de alocação escolhida
                switch (politica) {
                    case '1':
                        gerenciador.primeiroAjuste(tamanho);
                        break;
                    case 'M':
                        gerenciador.melhorAjuste(tamanho);
                        break;
                    case 'P':
                        gerenciador.piorAjuste(tamanho);
                        break;
                }

            }  else if (instrucao == 'L') { //Libera memória
                System.out.print("\nDigite a quantidade de KB: ");
                int tamanho = sc.nextInt();
                gerenciador.liberarMemoria(tamanho);

            } else if (instrucao != 'X') { //Instrução inválida
                System.out.println("Instrucao invalida!");
            }

            //Exibe o estado atual da memória após cada operação
            if (instrucao != 'X') {
                System.out.println("======================================================");
                System.out.println("Memoria Atual: (false para ocupado, true para livre)");
                gerenciador.exibirMemoria();
                System.out.println("======================================================");
            }
        } while (instrucao != 'X');
        
        sc.close();
    }
}