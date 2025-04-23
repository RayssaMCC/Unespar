import java.util.Scanner;

public class MenuCI {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcao;
        
        ControladorCI controlador = new ControladorCI();

        //Mostra o menu de opções e executa a opção escolhida pelo usuário
        do {
            System.out.println("================================================================");
            System.out.println("\tOPÇOES:");
            System.out.println("================================================================");
            System.out.println("1 - Inserir instruçao");
            System.out.println("2 - Executar instruçao");
            System.out.println("3 - Ver instruçoes");
            System.out.println("4 - Sair");
            System.out.println("================================================================");
            System.out.print("Escolha uma opçao: ");
            opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao) {
                case 1:
                    controlador.entradaUsuario();
                    break;
                case 2:
                    controlador.executarTodasInstrucoes();
                    break;
                case 3:
                    controlador.mostrarInstrucoes();
                    break;
                case 4:
                    System.out.println("Programa encerrado.");
                    break;
                default:
                    System.out.println("Opçao invalida!");
                    break;
            }

        } while (opcao != 4);

        sc.close();
    }
}