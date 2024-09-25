package Atividade.Conta;
public class Conta {
    private int id;
    private String nome;
    private double saldo;
    private String tipo;

    // Getters e Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    // Método para exibir informações da conta
    public String toString() {
        return "Conta [id=" + id + ", nome=" + nome + ", saldo=" + saldo + ", tipo=" + tipo + "]";
    }
}
