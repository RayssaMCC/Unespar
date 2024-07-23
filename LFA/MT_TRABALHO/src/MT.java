import java.util.Scanner;
import java.util.HashMap;

public class MT{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        //Quantidade de letras do alfabeto e tratamento de erro
        System.out.println("Digite a quantidade de letras do alfabeto:");
        int qtdLetrasAlfabeto = 0;
        boolean validInput = false;
        while (!validInput) {
            try {
                qtdLetrasAlfabeto = Integer.parseInt(sc.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.println("Valor inválido. Digite novamente a quantidade de letras do alfabeto:");
            }
        }

        //Vetor que armazena as letras do alfabeto
        String letrasAlfabeto[] = new String[qtdLetrasAlfabeto];
        for (int i = 0; i < qtdLetrasAlfabeto; i++) {
            System.out.println("Digite a " + (i + 1) + " letra do alfabeto:");
            letrasAlfabeto[i] = sc.nextLine();
        }

        //Quantidade de letras do alfabeto auxiliar e tratamento de erro
        System.out.println("Digite a quantidade de letras do alfabeto auxiliar:");
        int qtdLetrasAlfabetoAuxiliar = 0;
        validInput = false;
        while (!validInput) {
            try {
                qtdLetrasAlfabetoAuxiliar = Integer.parseInt(sc.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.println("Valor inválido. Digite novamente a quantidade de letras do alfabeto auxiliar:");
            }
        }

        //Vetor que armazena as letras do alfabeto auxiliar
        String letrasAlfabetoAuxiliar[] = new String[qtdLetrasAlfabetoAuxiliar];
        for (int i = 0; i < qtdLetrasAlfabetoAuxiliar; i++) {
            System.out.println("Digite a " + (i + 1) + " letra do alfabeto auxiliar:");
            letrasAlfabetoAuxiliar[i] = sc.nextLine();
        }

        //Quantidade de estados e tratamento de erro
        System.out.println("Digite a quantidade de estados:");
        int qtdEstados = 0;
        validInput = false;
        while (!validInput) {
            try {
                qtdEstados = Integer.parseInt(sc.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.println("Valor inválido. Digite novamente a quantidade de estados:");
            }
        }

        //Estado inicial e tratamento de erro
        System.out.println("Digite o estado inicial:");
        int estadoInicial = 0;
        validInput = false;
        while (!validInput) {
            try {
                estadoInicial = Integer.parseInt(sc.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.println("Valor inválido. Digite novamente o estado inicial:");
            }
        }

        //Quantidade de estados finais e tratamento de erro
        System.out.println("Digite a quantidade de estados finais:");
        int qtdEstadosFinais = 0;
        validInput = false;
        while (!validInput) {
            try {
                qtdEstadosFinais = Integer.parseInt(sc.nextLine());
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.println("Valor inválido. Digite novamente a quantidade de estados finais:");
            }
        }
        
        //Vetor que armazena os estados finais e tratamento de erro
        int estadoFinal[] = new int[qtdEstadosFinais];
        for (int i = 0; i < qtdEstadosFinais; i++) {
            System.out.println("Digite o estado final " + (i + 1) + ":");
            validInput = false;
            while (!validInput) {
                try {
                    estadoFinal[i] = Integer.parseInt(sc.nextLine());
                    validInput = true;
                } catch (NumberFormatException e) {
                    System.out.println("Valor inválido. Digite novamente o estado final:");
                }
            }
        }

        //Marcador de inicio
        System.out.println("Digite o marcador de inicio:");
        String marcadorInicio = sc.nextLine();

        //Marcador para branco
        System.out.println("Digite o marcador para branco:");
        String marcadorBranco = sc.nextLine();

        //Iserção da palavra que será testada
        System.out.println("Digite a palavra a ser testada: ");
        String palavra[] = sc.nextLine().split("");

        //Alocação da fita principal
        String fita[] = new String[100];
        alocarFita(fita, palavra, marcadorInicio, marcadorBranco);
        
        //Visualização da tabela de transição
        System.out.println("\n============== TABELA DE TRANSIÇAO ==============");
        System.out.print("   ");
        for (String i : letrasAlfabeto) {
            System.out.print(i + "   ");
        }
        for (String i : letrasAlfabetoAuxiliar) {
            System.out.print(i + "   ");
        }
        System.out.print(marcadorInicio + "   " + marcadorBranco + "\n");
        for (int i = 1; i < qtdEstados + 1; i++) {
            System.out.print("S" + i + " ");
            for (int j = 1; j < (qtdLetrasAlfabeto + qtdLetrasAlfabetoAuxiliar + 1 + 2); j++) {
                System.out.print( i +","+ j + " ");
            }
            System.out.println();
        }

        //HashMap que será usado pra salvar os estados presentes na execução dada pelo usuario
        HashMap<Integer, Estados> mapEstados = new HashMap<>();

        //Vetor que armazena o alfabeto geral
        String alfabetoGeral[] = new String[qtdLetrasAlfabeto + qtdLetrasAlfabetoAuxiliar + 2];
        int indiceAux_alfabetoGeral = 0;

        //Estrutura de repetição que preenche o vetor alfabetoGeral com as letras do alfabeto e do alfabeto auxiliar
        while (indiceAux_alfabetoGeral < alfabetoGeral.length) {
            for (String i : letrasAlfabeto) {
                alfabetoGeral[indiceAux_alfabetoGeral] = i;
                indiceAux_alfabetoGeral++;
            }
            for (String i : letrasAlfabetoAuxiliar) {
                alfabetoGeral[indiceAux_alfabetoGeral] = i;
                indiceAux_alfabetoGeral++;
            }
            alfabetoGeral[indiceAux_alfabetoGeral] = marcadorInicio;
            indiceAux_alfabetoGeral++;
            alfabetoGeral[indiceAux_alfabetoGeral] = marcadorBranco;
            indiceAux_alfabetoGeral++;
        }
        
        //Estrutura de repetição que preenche o HashMap com os estados presentes na execução dada pelo usuario
        for (int i = 1; i < (qtdEstados + 1); i++) {
            boolean encontrado = false;
            
            //Estrutura de repetição que verifica se o estado atual é um estado final
            for (int k = 0; k < estadoFinal.length; k++) {
                if (i == estadoFinal[k] && encontrado == false) {
                    Estados estado = new Estados(true);
                    mapEstados.put(i, estado);
                    encontrado = true;
                } else if (encontrado == false) {
                    Estados estado = new Estados(false);
                    mapEstados.put(i, estado);
                    encontrado = true;
                }
            }

            //Estrutura de repetição que preenche a tabela de transição com as informações dadas pelo usuario
            for (int j = 1; j <= (qtdLetrasAlfabeto + qtdLetrasAlfabetoAuxiliar + 2); j++) {
                System.out.println("----------------------------------------------------------------------");
                System.out.println("Digite o estado futuro da transiçao " + i + "," + j + ": (Coloque \"X\" ou \"x\" caso queira anular a transiçao)");
                String leitura = sc.nextLine();

                //Verifica se o campo foi anulado, caso contrario, preenche a tabela de transição com o alfabeto e direção
                if (leitura.equals("X") || leitura.equals("x")) {
                    System.out.println("O campo sera anulado!");
                } else {
                    int estadoFuturo = Integer.parseInt(leitura); 
                    System.out.println("Digite o alfabeto futuro da transiçao " + i + "," + j + ":");
                    String letraFutura = sc.nextLine();
                    System.out.println("Digite a direçao da transiçao " + i + "," + j + ": (D para Direita ou E para Esquerda)");
                    String direcao = sc.nextLine().toUpperCase();
    
                    //Define o que acontecerá na máquina, lendo o estado futuro, o alfabeto futuro e a direção
                    mapEstados.get(i).setTransicao(alfabetoGeral[j-1], letraFutura, direcao, estadoFuturo);
                }
            }
        }

        //VIsualização da tabela de transição final
        System.out.println();
        System.out.println("============== TABELA DE TRANSIÇAO FINAL ==============");
        System.out.print("   ");
        for (String i : alfabetoGeral) {
            System.out.print(i + "       ");
        }
        System.out.println();
        for (int i = 1; i < qtdEstados + 1; i++) {
            System.out.print("S" + i + " ");
            for (int j = 1; j < (qtdLetrasAlfabeto + qtdLetrasAlfabetoAuxiliar + 1 + 2); j++) {
                System.out.print(((mapEstados.get(i).getTransicao(alfabetoGeral[j-1])) == null ? "":("S" + mapEstados.get(i).getTransicao(alfabetoGeral[j-1]).getEstadoFuturo()) + ","));
                System.out.print(((mapEstados.get(i).getTransicao(alfabetoGeral[j-1])) == null ? "":(mapEstados.get(i).getTransicao(alfabetoGeral[j-1]).getAlfabetoFuturo()) + ","));
                System.out.print(((mapEstados.get(i).getTransicao(alfabetoGeral[j-1])) == null ? "X       ":(mapEstados.get(i).getTransicao(alfabetoGeral[j-1]).getDirecao()) + "  "));
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("----------------------------------------------------------------------");

        //Execução da máquina de turing
        executarMT(fita, mapEstados, estadoInicial);

        System.out.println();
        
        //Estrutura de repetição que permite o usuário testar mais de uma palavra
        boolean aux = true;
        while (aux) {
            System.out.println("Deseja testar outra palavra? (S/N)");
            String resposta = sc.nextLine().toUpperCase();

            if (resposta.equals("S")) {
                System.out.println("Digite a nova palavra: ");
                String nova_palavra[] = sc.nextLine().split("");
                alocarFita(fita, nova_palavra, marcadorInicio, marcadorBranco);
                System.out.println();
                executarMT(fita, mapEstados, estadoInicial);
                System.out.println();
            } else if (resposta.equals("N")) {
                aux = false;
                System.out.println("Programa encerrado.");
            } else {
                System.out.println("Resposta inválida. Digite 'S' para sim ou 'N' para nao.");
            }
        }
        sc.close();
    }

    //Método que aloca a palavra na fita principal
    public static String[] alocarFita(String fita[], String palavra[], String marcadorInicio, String marcadorBranco) {
        for (int i = 0; i < fita.length; i++) {
            if (i == 0) {
                fita[i] = marcadorInicio; //Marcador de início na posição 0
            } else {
                fita[i] = marcadorBranco; //Marcador de branco nas demais posições
            }
        }
        
        //Estrutura de repetição que coloca a palavra na fita principal
        for (int i = 0; i < palavra.length; i++) {
            fita[i+1] = palavra[i];
        }
        return fita;
    }

    //Método que executa a máquina de turing
    public static void executarMT(String[] fita, HashMap<Integer, Estados> mapEstados, int estadoInicial) {
        //Cópia da fita principal
        String fitaFinal[] = new String[fita.length];
        for (int i = 0; i < fitaFinal.length; i++) {
            fitaFinal[i] = fita[i];
        }
        
        Transicao transicaoAtual = new Transicao();
        int posAtualFita = 1; //Posição atual da fita é 1 pois a posição 0 é o marcador de início
        int estadoAtual = estadoInicial;
        boolean aux = true;
    
        //Estrutura de repetição que executa a máquina de turing
        while (aux) {
            //Verifica se a posição atual na fita está dentro dos limites da fita
            if (posAtualFita < 0 || posAtualFita >= fitaFinal.length) {
                aux = false;
                System.out.println("Erro: Acesso fora dos limites da fita.");
                break; //Sai do loop para evitar exceção de índice fora dos limites
            }
    
            //Verifica se a transição é nula, caso contrário, executa a transição
            if (mapEstados.get(estadoAtual).getTransicao(fitaFinal[posAtualFita]) == null) {
                aux = false;
                System.out.println("Palavra nao aceita!");
            } else {
                transicaoAtual = mapEstados.get(estadoAtual).getTransicao(fitaFinal[posAtualFita]); 
                fitaFinal[posAtualFita] = transicaoAtual.getAlfabetoFuturo(); //Altera o alfabeto atual para o alfabeto futuro
                estadoAtual = transicaoAtual.getEstadoFuturo(); //Altera o estado atual para o estado futuro
    
                //Move a cabeça de leitura/gravação com base na direção
                if (transicaoAtual.getDirecao().equals("D")) {
                    posAtualFita++;
                } else if (transicaoAtual.getDirecao().equals("E")) {
                    posAtualFita--;
                }

                //Passo a passo da fita
                for(String i : fitaFinal){
                    System.out.print(i);
                }
                System.out.println();
                for(int i = 0; i <= posAtualFita; i++){
                    System.out.print(i == posAtualFita ? "^":" ");
                }
                System.out.println();
    
                //Verifica se é um estado final
                if (mapEstados.get(estadoAtual).getEstadoFinal()) {
                    aux = false;
                    System.out.println("Palavra aceita!");
                }
            }
        }

        //Imprime a fita inicial
        System.out.println("Fita inicial: ");
        for (String i : fita) {
            System.out.print(i);
        }
        System.out.println("\n");

        //Imprime a fita final
        System.out.println("Fita final: ");
        for (String i : fitaFinal) {
            System.out.print(i);
        }
        System.out.println("\n----------------------------------------------------------------------");
    }
}