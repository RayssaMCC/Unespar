package contas2;

public class Conta {

    protected double saldo;

    public void mostrarSaldo() {
        System.out.printf("Saldo: R$ %.2f%n", saldo);
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public void sacar(double valor) {

        if (valor <= saldo) {
            saldo -= valor;
        } else {
            System.out.println("Saldo insuficiente.");
        }
    }

    public void atualiza(double taxa) {
        saldo += saldo * taxa;
    }
}
