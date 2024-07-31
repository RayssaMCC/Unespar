import java.util.*;

public class ControladorCI implements InterfaceCI {
    private Scanner sc = new Scanner(System.in); //Scanner para entrada de dados/instruções
    private int PC = 1; //Contador de programa que armazena a posição da instrução atual
    private int MBR = 0; //Registrador de memória
    private int[] memoria = new int[1000]; //Memória de 1000 posições para os dados das instruções 
    private boolean flagZero = false; //Flag para verificar se o MBR é zero
    private boolean flagNegativo = false; //Flag para verificar se o MBR é negativo
    private List<String> instrucoes = new ArrayList<String>(); //Lista de strings para armazenar as instruções

    //Recebe as instruções do usuário e armazena na lista 
    public void entradaUsuario() {
        instrucoes.add("x"); //Adiciona um valor qualquer para iniciar a lista de instruções como 1, seguindo o PC
        System.out.println("Digite as instruçoes (ou '4' para finalizar a inserçao de dados):");

        //O loop é interrompido quando o usuário digita 4 e retorna ao menu de opções
        while (true) {

            System.out.println("\nInsira o codigo da instruçao:");
            String instrucao = sc.nextLine();

            //Verifica se a instrução inserida é válida e solicita os operandos ao usuário
            if (instrucao.equals("000001") || instrucao.equals("000010") || instrucao.equals("000011") || instrucao.equals("000100") || instrucao.equals("000101") || 
                instrucao.equals("000110") || instrucao.equals("000111") || instrucao.equals("001000") || instrucao.equals("001001") || 
                instrucao.equals("001010") || instrucao.equals("001011") || instrucao.equals("001111") || instrucao.equals("001100")) {

                String op1 = "",  op2 = ""; //Armazena os operandos da instrução, "" para iniciarem vazios
                
                //Se o código da instrução for diferente de 001010, 001011 e 001100, solicita o primeiro operando ao usuário
                if (!instrucao.equals("001010") && !instrucao.equals("001011") && !instrucao.equals("001100")) {
                    System.out.print("Digite o primeiro operando: "); 
                    op1 = sc.nextLine();

                    //Se o código da instrução for 000010, solicita o segundo operando ao usuário
                    if (instrucao.equals("000010")) {
                        System.out.print("Digite o segundo operando: ");
                        op2 = sc.nextLine();
                    }
                }

                instrucoes.add(instrucao + " " + op1 + " " + op2); //Adiciona a instrução na lista

            } else if (instrucao.equals("4")) {
                System.out.println("Inserçao de instruçoes finalizada.");
                break;
            } else {
                System.out.println("Instruçao invalida!");
            }
        }
    }

    //Mostra a tabela de instruções e as instruções inseridas
    public void mostrarInstrucoes() {
        System.out.println("================================================================");
        System.out.printf("\tINSTRUÇOES\n");
        System.out.println("================================================================");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "COD", "OP1", "OP2", "RESULTADOS");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "000001", "#POS", "-", "MBR <- #POS");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "000010", "#POS", "#DADO", "POS <- #DADO");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "000011", "#POS", "-", "MBR <- MBR + #POS");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "000100", "#POS", "-", "MBR <- MBR - #POS");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "000101", "#POS", "-", "MBR <- MBR * #POS");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "000110", "#POS", "-", "MBR <- MBR / #POS");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "000111", "#LIN", "-", "JUMP to #LIN");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "001000", "#LIN", "-", "JUMP IF Z to #LIN");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "001001", "#LIN", "-", "JUMP IF N to #LIN");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "001010", "-", "-", "MBR <- raiz_quadrada(MBR)");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "001011", "-", "-", "MBR <- -MBR");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "001111", "#POS", "-", "#POS <- MBR");
        System.out.printf("%-7s%-7s%-7s%-20s\n", "001100", "-", "-", "NOP");
        System.out.println("================================================================");

        //Exibe as instruções e operandos que já foram inseridos pelo usuário
        System.out.println("Instruçoes inseridas atualmente (codigo op1 op2):");
        for (int i = 1; i < instrucoes.size(); i++) {
            System.out.println(instrucoes.get(i));
        }
    }

    //Executa as instruções de acordo com o código inserido
    private void executarInstrucao(String instrucao) {
        String[] componentesInstrucao = instrucao.split(" "); //Separa a instrução em componentes para pegar o código e os operandos e executar a instrução
        String codigo = componentesInstrucao[0]; //Atualiza o código atual com o código da instrução futura para executar a instrução correta e exibir o ciclo de instrução
        //[0] - código da instrução       [1] - operando 1           [2] - operando 2

        //Converte as strings de operandos para inteiro e chama as instruções para cada código
        switch (codigo) {
            case "000001": //MBR <- #pos
                instrucao000001(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "000010": //#pos <- #dado
                instrucao000010(Integer.parseInt(componentesInstrucao[1]), Integer.parseInt(componentesInstrucao[2]));
                break;
            case "000011": //MBR <- MBR + #pos
                instrucao000011(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "000100": //MBR <- MBR - #pos
                instrucao000100(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "000101": //MBR <- MBR * #pos
                instrucao000101(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "000110": //MBR <- MBR / #pos
                instrucao000110(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "000111": //JUMP to #lin
                instrucao000111(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "001000": //JUMP IF Z to #lin
                instrucao001000(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "001001": //JUMP IF N to #lin
                instrucao001001(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "001010": //MBR <- raiz_quadrada(MBR)
                instrucao001010();
                break;
            case "001011": //MBR <- -MBR
                instrucao001011();
                break;
            case "001111": //#pos <- MBR
                instrucao001111(Integer.parseInt(componentesInstrucao[1]));
                break;
            case "001100": //NOP
                instrucao001100();
                break;
            default: //Instrução inválida
                System.out.println("Instruçao invalida!");
                break;
        }
    }

    //Mostra o ciclo de instrução
    private void mostrarCiclo() {
        String[] componentesInstrucao = instrucoes.get(PC).split(" "); //Divide a instrução atual em componentes baseado em espaços
        String codigo = componentesInstrucao[0]; //O primeiro componente é sempre o código da operação
        String op1 = componentesInstrucao.length > 1 ? componentesInstrucao[1] : "N/A"; //O segundo componente, se existir, é o primeiro operando
        String op2 = componentesInstrucao.length > 2 ? componentesInstrucao[2] : "N/A"; //O terceiro componente, se existir, é o segundo operando
        

        //Exibe os componentes da instrução
        System.out.println("================================================================");
        System.out.println("CALCULO DO ENDEREÇO DA INSTRUÇAO:");
        System.out.printf("PC: %06d\n", PC);

        System.out.println("\nBUSCANDO A INSTRUÇAO:");
        System.out.println("<OPCODE>: " + codigo);
        System.out.println("<OP1>: " + op1);
        System.out.println("<OP2>: " + op2);

        System.out.println("\nDECODIFICANDO A INSTRUÇAO:");
        switch (codigo) {
            case "000001":
                System.out.println("MBR <- #POS");
                System.out.println(MBR + " <- #" + op1);
                break;
            case "000010":
                System.out.println("#POS <- #DADO");
                System.out.println(op1 + " <- " + op2);
                break;
            case "000011":
                System.out.println("MBR <- MBR + #POS");
                System.out.println(MBR + " <- " + MBR + " + #" + op1);
                break;
            case "000100":
                System.out.println("MBR <- MBR - #POS");
                System.out.println(MBR + " <- " + MBR + " - #" + op1);
                break;
            case "000101":
                System.out.println("MBR <- MBR * #POS");
                System.out.println(MBR + " <- " + MBR + " * #" + op1);
                break;
            case "000110":
                System.out.println("MBR <- MBR / #POS");
                System.out.println(MBR + " <- " + MBR + " / #" + op1);
                break;
            case "000111":
                System.out.println("JUMP to #LIN");
                System.out.println("JUMP to #" + op1);
                break;
            case "001000":
                System.out.println("JUMP IF Z to #LIN");
                System.out.println("JUMP IF Z to #" + op1);
                break;
            case "001001":
                System.out.println("JUMP IF N to #LIN");
                System.out.println("JUMP IF N to #" + op1);
                break;
            case "001010":
                System.out.println("MBR <- sqrt(MBR)");
                System.out.println("MBR <- sqrt(" + MBR + ")");
                break;
            case "001011":
                System.out.println("MBR <- -MBR");
                System.out.println("MBR <- -" + MBR);
                break;
            case "001111":
                System.out.println("#POS <- MBR");
                System.out.println(op1 + " <- " + MBR);
                break;
            case "001100":
                System.out.println("NOP");
                break;
            default:
                System.out.println("CODIGO DE INSTRUÇAO NAO RECONHECIDO.");
                break;
        }

        System.out.println("\nCALCULO DO ENDEREÇO DO OPERANDO:");
        System.out.println("Endereço: " + op1);
        System.out.println("\nBUSCANDO O OPERANDO NA POSIÇAO:");
        System.out.println("MAR: " + op1);

        //Se o segundo operando existir, exibe o cálculo do endereço e busca o operando na posição
        if (!op2.isEmpty()) {
            System.out.println("\nCALCULO DO ENDEREÇO DO SEGUNDO OPERANDO:");
            System.out.println("Endereço: " + op2);
            System.out.println("\nBUSCANDO O SEGUNDO OPERANDO NA POSIÇAO:");
            System.out.println("MAR: " + op2);
        }

        System.out.println("\nOPERAÇAO DE DADOS:");
        switch (codigo) {
            case "000001": //MBR <- #pos
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR NA MEMORIA: " + memoria[Integer.parseInt(op1)]);
                System.out.println("VALOR DO MBR APOS A OPERAÇAO: " + MBR + " + " + memoria[Integer.parseInt(op1)] + " = " + (MBR + memoria[Integer.parseInt(op1)])); 
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "000010": //#pos <- #dado
                System.out.println("ARMAZENANDO: " + op2);
                System.out.println("NA POSIÇAO: " + op1);
                System.out.println("\nCALCULANDO ENDEREÇO DO OPERANDO:");
                System.out.println("ENDEREÇO: " + op1);
                System.out.println("\nARMAZENANDO O OPERANDO:");
                System.out.println("MAR: " + op1);
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "000011": //MBR <- MBR + #pos
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR DO CONTEUDO NA POSIÇAO: " + memoria[Integer.parseInt(op1)]);
                System.out.println("VALOR DO MBR APOS A OPERAÇAO: " + MBR + " + " + memoria[Integer.parseInt(op1)] + " = " + (MBR + memoria[Integer.parseInt(op1)])); //Transforma em inteiro e divide
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "000100": //MBR <- MBR - #pos
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR DO CONTEUDO NA POSIÇAO: " + memoria[Integer.parseInt(op1)]);
                System.out.println("VALOR DO MBR APOS A OPERAÇAO: " + MBR + " - " + memoria[Integer.parseInt(op1)] + " = " + (MBR - memoria[Integer.parseInt(op1)])); //Transforma em inteiro e divide
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "000101": //MBR <- MBR * #pos
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR DO CONTEUDO NA POSIÇAO: " + memoria[Integer.parseInt(op1)]);
                System.out.println("VALOR DO MBR APOS A OPERAÇAO: " + MBR + " * " + memoria[Integer.parseInt(op1)] + " = " + (MBR * memoria[Integer.parseInt(op1)])); //Transforma em inteiro e divide
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "000110": //MBR <- MBR / #pos
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR DO CONTEUDO NA POSIÇAO: " + memoria[Integer.parseInt(op1)]);
                System.out.println("VALOR DO MBR APOS A OPERAÇAO: " + MBR + " / " + memoria[Integer.parseInt(op1)] + " = " + (MBR / memoria[Integer.parseInt(op1)])); //Transforma em inteiro e divide
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "000111": //JUMP to #lin
                System.out.println("PULANDO PARA A LINHA: " + op1);
                break;
            case "001000": //JUMP IF Z to #lin
                if (flagZero) {
                    System.out.println("PULANDO PARA A LINHA: " + op1);
                } else {
                    System.out.println("NAO PULOU PARA A LINHA: " + op1);
                }
                break;
            case "001001": //JUMP IF N to #lin
                if (flagNegativo) {
                    System.out.println("PULANDO PARA A LINHA: " + op1);
                } else {
                    System.out.println("NAO PULOU PARA A LINHA: " + op1);
                }
                break;
            case "001010": //MBR <- raiz_quadrada(MBR)
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR DO MBR APOS A OPERAÇAO: " + Math.sqrt(MBR));
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "001011": //MBR <- -MBR
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR DO MBR APOS A OPERAÇAO: " + (-MBR));
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "001111": //#pos <- MBR
                System.out.println("VALOR DO MBR: " + MBR);
                System.out.println("VALOR DO ENDEREÇO APOS A OPERAÇAO " + MBR);
                System.out.println("O VALOR FOI ARMAZENADO!");
                break;
            case "001100": //NOP
                System.out.println("ENCERRANDO OPERAÇAO DE DADOS");
                System.out.println("OPERAÇAO FINALIZADA!");
                System.exit(0);
                break;
            default:
                break;
        }
        System.out.println("================================================================");
    }

    //Executa todas as instruções armazenadas na lista de instruções e exibe o ciclo de instrução
    public void executarTodasInstrucoes() {
        System.out.println("================================================================");
        System.out.println("\tEXECUTANDO INSTRUÇOES");
        while (PC < instrucoes.size()) { //Executa enquanto o PC não passar do tamanho da lista de instruções
            mostrarCiclo();
            executarInstrucao(instrucoes.get(PC)); //Executa a instrução atual
        }
    }

    //Métodos para executar as instruções de acordo com o código
    private void instrucao000001(int pos) {
        MBR = memoria[pos];
        PC++;
    }

    private void instrucao000010(int pos, int dado) {
        memoria[pos] = dado;
        PC++;
    }

    private void instrucao000011(int pos) {
        MBR += memoria[pos];
        PC++;
    }

    private void instrucao000100(int pos) {
        MBR -= memoria[pos];
        PC++;
    }

    private void instrucao000101(int pos) {
        MBR *= memoria[pos];
        PC++;
    }

    private void instrucao000110(int pos) {
        MBR /= memoria[pos];
        PC++;
    }

    private void instrucao000111(int lin) {
        PC = lin;
    }

    private void instrucao001000(int lin) {
        flagZero = (MBR == 0);
        if (flagZero) {
            PC = lin;
        } else {
            PC++;
        }
    }

    private void instrucao001001(int lin) {
        flagNegativo = (MBR < 0);
        if (flagNegativo) {
            PC = lin;
        } else {
            PC++;
        }
    }

    private void instrucao001010() {
        MBR = (int) Math.sqrt(MBR);
        PC++;
    }

    private void instrucao001011() {
        MBR = -MBR;
        PC++;
    }

    private void instrucao001111(int pos) {
        memoria[pos] = MBR;
        PC++;
    }

    private void instrucao001100() {
        //NOP, aparece no switch case
    }
}