//TRANSFORMAR O SWITCH CASE DE OPCODE EM CLASSES PRA FACILITAR DEBUG
//inserir
//ver instrução
//executar



import java.util.HashMap;
import java.util.Map;

public class SimuladorCiclosInstrucoes {

    // Registradores
    private int PC; // Program Counter
    private int IR; // Instruction Register
    private int MAR; // Memory Address Register
    private int MBR; // Memory Buffer Register
    private boolean flagZero;
    private boolean flagNegativo;

    // Memória (endereço -> valor)
    private Map<Integer, Integer> memoria;

    public SimuladorCiclosInstrucoes() {
        PC = 0;
        IR = 0;
        MAR = 0;
        MBR = 0;
        flagZero = false;
        flagNegativo = false;
        memoria = new HashMap<>();
    }

    // Método para carregar instruções na memória
    public void carregarInstrucao(int endereco, int instrucao) {
        memoria.put(endereco, instrucao);
    }

    // Método para carregar dados na memória
    public void carregarDado(int endereco, int dado) {
        memoria.put(endereco, dado);
    }

    // Método para simular a execução das instruções
    public void executar() {
        while (true) {
            IR = memoria.get(PC); // Busca da instrução
            PC++;
            int opcode = (IR >> 16) & 0xFF;
            int operando1 = (IR >> 8) & 0xFF;
            int operando2 = IR & 0xFF;

            switch (opcode) {
                case 0x01: // MBR ← #pos
                    MBR = memoria.get(operando1);
                    break;
                case 0x02: // #pos ← #dado
                    memoria.put(operando1, operando2);
                    break;
                case 0x03: // MBR ← MBR + #pos
                    MBR += memoria.get(operando1);
                    break;
                case 0x04: // MBR ← MBR - #pos
                    MBR -= memoria.get(operando1);
                    break;
                case 0x05: // MBR ← MBR * #pos
                    MBR *= memoria.get(operando1);
                    break;
                case 0x06: // MBR ← MBR / #pos
                    MBR /= memoria.get(operando1);
                    break;
                case 0x07: // JUMP to #lin
                    PC = operando1;
                    break;
                case 0x08: // JUMP IF Z to #lin
                    if (flagZero) {
                        PC = operando1;
                    }
                    break;
                case 0x09: // JUMP IF N to #lin
                    if (flagNegativo) {
                        PC = operando1;
                    }
                    break;
                case 0x0A: // MBR ← sqrt(MBR)
                    MBR = (int) Math.sqrt(MBR);
                    break;
                case 0x0B: // MBR ← -MBR
                    MBR = -MBR;
                    break;
                case 0x0C: // #pos ← MBR
                    memoria.put(operando1, MBR);
                    break;
                case 0x0F: // NOP (No operation)
                    break;
                default:
                    System.out.println("Instrução inválida: " + opcode);
                    return;
            }

            flagZero = (MBR == 0);
            flagNegativo = (MBR < 0);

            imprimirEstadoRegistradores();

            if (opcode == 0x0F) { // NOP - fim da execução
                break;
            }
        }
    }

    // Método para imprimir o estado dos registradores
    private void imprimirEstadoRegistradores() {
        System.out.println("PC: " + PC);
        System.out.println("IR: " + IR);
        System.out.println("MAR: " + MAR);
        System.out.println("MBR: " + MBR);
        System.out.println("Flag Zero: " + flagZero);
        System.out.println("Flag Negativo: " + flagNegativo);
        System.out.println();
    }

    public static void main(String[] args) {
        SimuladorCiclosInstrucoes simulador = new SimuladorCiclosInstrucoes();
        
        // Carregando programa de exemplo na memória
        simulador.carregarInstrucao(0, 0x0200FB05); // Armazena 5 na posição 251
        simulador.carregarInstrucao(1, 0x0200FC0A); // Armazena 10 na posição 252
        simulador.carregarInstrucao(2, 0x0200FD0F); // Armazena 15 na posição 253
        simulador.carregarInstrucao(3, 0x0100FB00); // MBR recebe o conteúdo da posição 251
        simulador.carregarInstrucao(4, 0x0300FC00); // MBR recebe o conteúdo dele mesmo somado com o conteúdo da posição 252
        simulador.carregarInstrucao(5, 0x0300FD00); // MBR recebe o conteúdo dele mesmo somado com o conteúdo da posição 253
        simulador.carregarInstrucao(6, 0x0C00FE00); // Posição 254 recebe o conteúdo do MBR
        simulador.carregarInstrucao(7, 0x0F000000); // Fim, no operation

        simulador.executar();
    }
}












/*import java.util.*;

public class SimuladorCiclosInstrucoes {

    // Registradores
    private int PC; // Program Counter
    private int IR; // Instruction Register
    private int MAR; // Memory Address Register
    private int MBR; // Memory Buffer Register
    private boolean flagZero;
    private boolean flagNegativo;

    // Memória (endereço -> valor)
    private Map<Integer, Integer> memoria;
    private List<String> operacoesRealizadas;

    public SimuladorCiclosInstrucoes() {
        PC = 0;
        IR = 0;
        MAR = 0;
        MBR = 0;
        flagZero = false;
        flagNegativo = false;
        memoria = new HashMap<>();
        operacoesRealizadas = new ArrayList<>();
    }

    // Método para carregar instruções na memória
    public void carregarInstrucao(int endereco, int instrucao) {
        memoria.put(endereco, instrucao);
    }

    // Método para carregar dados na memória
    public void carregarDado(int endereco, int dado) {
        memoria.put(endereco, dado);
    }

    // Método para simular a execução das instruções
    public void executar() {
        while (true) {
            IR = memoria.getOrDefault(PC, 0); // Busca da instrução
            PC++;
            int opcode = (IR >> 16) & 0xFF;
            int operando1 = (IR >> 8) & 0xFF;
            int operando2 = IR & 0xFF;

            String operacao = "";

            switch (opcode) {
                case 0x01: // MBR ← #pos
                    MBR = memoria.get(operando1);
                    operacao = "MBR recebe o conteúdo da posição " + operando1;
                    break;
                case 0x02: // #pos ← #dado
                    memoria.put(operando1, operando2);
                    operacao = "Armazena " + operando2 + " na posição " + operando1;
                    break;
                case 0x03: // MBR ← MBR + #pos
                    MBR += memoria.get(operando1);
                    operacao = "MBR recebe o conteúdo dele mesmo somado com o conteúdo da posição " + operando1;
                    break;
                case 0x04: // MBR ← MBR - #pos
                    MBR -= memoria.get(operando1);
                    operacao = "MBR recebe o conteúdo dele mesmo subtraído pelo conteúdo da posição " + operando1;
                    break;
                case 0x05: // MBR ← MBR * #pos
                    MBR *= memoria.get(operando1);
                    operacao = "MBR recebe o conteúdo dele mesmo multiplicado pelo conteúdo da posição " + operando1;
                    break;
                case 0x06: // MBR ← MBR / #pos
                    MBR /= memoria.get(operando1);
                    operacao = "MBR recebe o conteúdo dele mesmo dividido pelo conteúdo da posição " + operando1;
                    break;
                case 0x07: // JUMP to #lin
                    PC = operando1;
                    operacao = "JUMP para a linha " + operando1;
                    break;
                case 0x08: // JUMP IF Z to #lin
                    if (flagZero) {
                        PC = operando1;
                    }
                    operacao = "JUMP IF Z para a linha " + operando1;
                    break;
                case 0x09: // JUMP IF N to #lin
                    if (flagNegativo) {
                        PC = operando1;
                    }
                    operacao = "JUMP IF N para a linha " + operando1;
                    break;
                case 0x0A: // MBR ← sqrt(MBR)
                    MBR = (int) Math.sqrt(MBR);
                    operacao = "MBR recebe a raiz quadrada de MBR";
                    break;
                case 0x0B: // MBR ← -MBR
                    MBR = -MBR;
                    operacao = "MBR recebe o valor negativo de MBR";
                    break;
                case 0x0C: // #pos ← MBR
                    memoria.put(operando1, MBR);
                    operacao = "Posição " + operando1 + " recebe o conteúdo de MBR";
                    break;
                case 0x0F: // NOP (No operation)
                    operacao = "NOP - No operation";
                    break;
                default:
                    System.out.println("Instrução inválida: " + opcode);
                    return;
            }

            flagZero = (MBR == 0);
            flagNegativo = (MBR < 0);

            operacoesRealizadas.add(operacao);
            imprimirEstadoRegistradores();

            if (opcode == 0x0F) { // NOP - fim da execução
                break;
            }
        }
    }

    // Método para imprimir o estado dos registradores
    private void imprimirEstadoRegistradores() {
        System.out.println("PC: " + PC);
        System.out.println("IR: " + IR);
        System.out.println("MAR: " + MAR);
        System.out.println("MBR: " + MBR);
        System.out.println("Flag Zero: " + flagZero);
        System.out.println("Flag Negativo: " + flagNegativo);
        System.out.println();
    }

    // Método para exibir todas as operações realizadas
    private void exibirOperacoesRealizadas() {
        System.out.println("Operações realizadas:");
        for (String operacao : operacoesRealizadas) {
            System.out.println(operacao);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        SimuladorCiclosInstrucoes simulador = new SimuladorCiclosInstrucoes();

        System.out.println("Insira as instruções no formato opcode operando1 operando2, separados por espaço. Insira 'end' para terminar.");
        int endereco = 0;
        while (true) {
            System.out.print("Instrução " + (endereco + 1) + ": ");
            String input = scanner.nextLine();
            if (input.equals("end")) {
                break;
            }
            String[] parts = input.split(" ");
            if (parts.length != 3) {
                System.out.println("Entrada inválida. Por favor, insira no formato correto.");
                continue;
            }
            int opcode = Integer.parseInt(parts[0], 16);
            int operando1 = Integer.parseInt(parts[1], 16);
            int operando2 = Integer.parseInt(parts[2], 16);
            int instrucao = (opcode << 16) | (operando1 << 8) | operando2;
            simulador.carregarInstrucao(endereco, instrucao);
            endereco++;
        }

        simulador.executar();
        simulador.exibirOperacoesRealizadas();
    }
}
 */








 


 /*import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class GeneralSimulator {

    // Registradores
    private int PC; // Program Counter
    private int IR; // Instruction Register
    private int MAR; // Memory Address Register
    private int MBR; // Memory Buffer Register
    private boolean flagZero;
    private boolean flagNegativo;

    // Memória (endereço -> valor)
    private Map<Integer, Integer> memoria;

    public GeneralSimulator() {
        PC = 0;
        IR = 0;
        MAR = 0;
        MBR = 0;
        flagZero = false;
        flagNegativo = false;
        memoria = new HashMap<>();
    }

    // Método para carregar instruções na memória
    public void carregarInstrucao(int endereco, int instrucao) {
        memoria.put(endereco, instrucao);
    }

    // Método para carregar dados na memória
    public void carregarDado(int endereco, int dado) {
        memoria.put(endereco, dado);
    }

    // Método para simular a execução das instruções
    public void executar() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter instructions in the format 'opcode operand1 operand2' (Enter 'exit' to stop):");

        while (true) {
            String input = scanner.nextLine();

            if (input.equals("exit")) {
                break;
            }

            String[] parts = input.split(" ");
            int opcode = Integer.parseInt(parts[0], 16);
            int operando1 = Integer.parseInt(parts[1], 16);
            int operando2 = Integer.parseInt(parts[2], 16);

            switch (opcode) {
                case 0x01:
                    MBR = memoria.get(operando1);
                    break;
                case 0x02:
                    memoria.put(operando1, operando2);
                    break;
                // Add more cases for other opcodes
                default:
                    System.out.println("Invalid instruction: " + opcode);
                    return;
            }

            flagZero = (MBR == 0);
            flagNegativo = (MBR < 0);

            imprimirEstadoRegistradores();
        }

        scanner.close();
    }

    // Método para imprimir o estado dos registradores
    private void imprimirEstadoRegistradores() {
        System.out.println("PC: " + PC);
        System.out.println("IR: " + IR);
        System.out.println("MAR: " + MAR);
        System.out.println("MBR: " + MBR);
        System.out.println("Flag Zero: " + flagZero);
        System.out.println("Flag Negativo: " + flagNegativo);
        System.out.println();
    }

    public static void main(String[] args) {
        GeneralSimulator simulator = new GeneralSimulator();
        simulator.executar();
    }
} */