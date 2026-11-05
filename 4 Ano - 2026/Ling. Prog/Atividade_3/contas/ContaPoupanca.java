package contas;

public class ContaPoupanca extends Conta {

    private int numConta;
    private int numAgencia;
    private int variacao;

    public void imprimirExtrato() {
        System.out.println("----- EXTRATO -----");
        System.out.println("Código: " + codigo);
        System.out.println("Proprietário: " + nomeProprietario);
        System.out.println("Número da conta: " + numConta);
        System.out.println("Número da agência: " + numAgencia);
        System.out.println("Variaçao: " + variacao);
        System.out.printf("Saldo: R$ %.2f%n", saldo);
        System.out.println("-------------------");
    }

    @Override
    public void somarSaldo(float s) {
        saldo += s;
    }

    public int getNumConta() {
        return numConta;
    }

    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }

    public int getNumAgencia() {
        return numAgencia;
    }

    public void setNumAgencia(int numAgencia) {
        this.numAgencia = numAgencia;
    }

    public int getVariacao() {
        return variacao;
    }

    public void setVariacao(int variacao) {
        this.variacao = variacao;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNomeProprietario() {
        return nomeProprietario;
    }

    public void setNomeProprietario(String nomeProprietario) {
        this.nomeProprietario = nomeProprietario;
    }

    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }
}