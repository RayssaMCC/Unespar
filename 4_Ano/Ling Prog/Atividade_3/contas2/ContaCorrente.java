package contas2;

public class ContaCorrente extends Conta {

    @Override
    public void atualiza(double taxa) {
        super.atualiza(taxa * 2);
    }

    @Override
    public void depositar(double valor) {
        saldo += valor - 0.10;
    }
}
