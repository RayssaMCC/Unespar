package excecao2;

public class Main {

    public static void main(String[] args) {

        Conta conta = new Conta("Rayssa", 500.00);

        System.out.println("Titular: " + conta.getTitular());
        System.out.println("Saldo inicial: R$ " + conta.getSaldo());

        try {

            System.out.println("\nTentando sacar R$ 200,00...");
            conta.saca(200.00);

            System.out.println("Saque realizado com sucesso.");
            System.out.println("Saldo atual: R$ " + conta.getSaldo());

            System.out.println("\nTentando sacar R$ 400,00...");
            conta.saca(400.00);

            System.out.println("Saque realizado com sucesso.");
            System.out.println("Saldo atual: R$ " + conta.getSaldo());

        } catch (ContaExcecao e) {

            System.out.println("Exceçao: " + e.getMessage());
            System.out.println("Saldo disponível: R$ " + conta.getSaldo());

        } finally {

            System.out.println("\nOperaçao finalizada.");
        }
    }
}
