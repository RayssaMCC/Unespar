import java.util.Scanner;

public class GerenciamentoDeMemoria {
    public static void imprimirBloco(int[] blocoMemoria) {
        // Imprime o bloco de memória após alteração
        System.out.println("--------------------------------------------------------------------------------------------------------------------");
        for (int i = 0; i < blocoMemoria.length; i++) {
            System.out.printf("|%d|\t", blocoMemoria[i]);
        }
        System.out.println("\n--------------------------------------------------------------------------------------------------------------------\n");
    }

    public static int[] alterarBloco(int[] blocoMemoria, int memoriaOcupar) {
        for (int i = 0; i < blocoMemoria.length; i++) {
            if (memoriaOcupar <= blocoMemoria[i]) {
                blocoMemoria[i] -= memoriaOcupar;
                if (blocoMemoria[i] == 0) {
                    System.out.printf("Bloco %d completamente utilizado.\n", i + 1);
                }
                return blocoMemoria;
            }
        }
        System.out.println("Nenhum bloco de memória possui memória suficiente para armazenar o valor desejado.\n");
        return blocoMemoria;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] blocoMemoria;
        int memoriaOcupar;

        System.out.println("Gerenciamento de Memória - First Fit");

        System.out.print("\nInforme a quantidade de blocos de memória: ");
        int tamanhoBloco = sc.nextInt();

        blocoMemoria = new int[tamanhoBloco];

        System.out.print("\nInforme o valor da memória disponível em cada bloco:\n");
        for (int i = 0; i < tamanhoBloco; i++) {
            System.out.printf("Bloco %d: ", i + 1);
            blocoMemoria[i] = sc.nextInt();
        }

        imprimirBloco(blocoMemoria);
        
        int controlador = 0;
        while (controlador == 0) {
            System.out.print("Insira o valor da memória a ser armazenada: ");
            memoriaOcupar = sc.nextInt();
            System.out.println();

            blocoMemoria = alterarBloco(blocoMemoria, memoriaOcupar);
            imprimirBloco(blocoMemoria);

            // Valida entrada: só aceita 0 ou 1
            while (true) {
                System.out.print("Digite 0 para alterar novamente a memória ou 1 para parar: ");
                controlador = sc.nextInt();
                if (controlador == 0 || controlador == 1) {
                    break;
                } else {
                    System.out.println("Entrada inválida! Digite apenas 0 (continuar) ou 1 (parar).\n");
                }
            }
        }
        sc.close();
    }
}
