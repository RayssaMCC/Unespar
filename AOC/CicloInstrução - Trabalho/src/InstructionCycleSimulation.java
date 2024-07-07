public class InstructionCycleSimulation {

    // Simula a etapa de Busca de Instrução
    public static String fetchInstruction(String[] instructions, int pc) {
        return instructions[pc]; // Retorna a instrução na posição do Contador de Programa (PC)
    }

    // Simula a etapa de Decodificação de Instrução
    public static String[] decodeInstruction(String instruction) {
        return instruction.split(" "); // Divide a instrução em partes (operação e operandos)
    }

    // Simula a etapa de Execução
    public static int executeInstruction(String[] decodedInstruction) {
        // Exemplo simples de execução: soma de dois números
        if ("ADD".equals(decodedInstruction[0])) {
            return Integer.parseInt(decodedInstruction[1]) + Integer.parseInt(decodedInstruction[2]);
        }
        return 0; // Retorna 0 para operações não reconhecidas
    }

    // Simula a etapa de Acesso à Memória (não aplicável neste exemplo simples)
    public static void memoryAccess() {
        // Neste exemplo, não há acesso à memória além da busca de instruções
    }

    // Simula a etapa de Escrita de Resultado
    public static void writeBack(int result) {
        System.out.println("Resultado da Execução: " + result);
    }

    public static void main(String[] args) {
        String[] instructions = {"ADD 5 3", "ADD 10 20"}; // Instruções de exemplo
        int pc = 0; // Contador de Programa

        while (pc < instructions.length) {
            String fetchedInstruction = fetchInstruction(instructions, pc); // Busca
            String[] decodedInstruction = decodeInstruction(fetchedInstruction); // Decodificação
            int result = executeInstruction(decodedInstruction); // Execução
            memoryAccess(); // Acesso à Memória
            writeBack(result); // Escrita de Resultado
            pc++; // Incrementa o Contador de Programa para a próxima instrução
        }
    }
}