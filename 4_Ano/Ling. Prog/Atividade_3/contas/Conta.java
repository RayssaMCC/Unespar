package contas;

public abstract class Conta {

    protected int codigo;
    protected String nomeProprietario;
    protected float saldo;

    public abstract void somarSaldo(float s);
}
