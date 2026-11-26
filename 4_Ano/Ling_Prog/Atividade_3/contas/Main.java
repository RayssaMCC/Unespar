package contas;

public class Main {

    public static void main(String[] args) {

        ContaPoupanca conta = new ContaPoupanca();

        conta.setCodigo(1);
        conta.setNomeProprietario("Rayssa");
        conta.setSaldo(500.00f);

        conta.setNumConta(12345);
        conta.setNumAgencia(100);
        conta.setVariacao(51);

        System.out.println("Extrato antes do depósito:");
        conta.imprimirExtrato();

        conta.somarSaldo(100.00f);

        System.out.println("\nExtrato depois de somar R$ 100,00:");
        conta.imprimirExtrato();
    }
}
