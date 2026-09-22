package contas2;

public class TestaContas {

    public static void main(String[] args) {

        Conta conta = new Conta();
        ContaCorrente corrente = new ContaCorrente();
        ContaPoupanca poupanca = new ContaPoupanca();

        // Depósitos
        conta.depositar(1000.00);
        corrente.depositar(1000.00);
        poupanca.depositar(1000.00);

        System.out.println("=== SALDOS INICIAIS ===");

        System.out.println("Conta:");
        conta.mostrarSaldo();

        System.out.println("Conta Corrente:");
        corrente.mostrarSaldo();

        System.out.println("Conta Poupança:");
        poupanca.mostrarSaldo();

        // Atualização com taxa de 1%
        double taxa = 0.01;

        conta.atualiza(taxa);
        corrente.atualiza(taxa);
        poupanca.atualiza(taxa);

        System.out.println("\n=== SALDOS APÓS ATUALIZAÇÃO ===");

        System.out.println("Conta:");
        conta.mostrarSaldo();

        System.out.println("Conta Corrente:");
        corrente.mostrarSaldo();

        System.out.println("Conta Poupança:");
        poupanca.mostrarSaldo();
    }
}