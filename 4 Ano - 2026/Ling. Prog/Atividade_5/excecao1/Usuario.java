package excecao1;

public class Usuario {

    private String nome;
    private double peso;
    private double altura;

    public Usuario(String nome, double peso, double altura) {
        this.nome = nome;
        this.peso = peso;
        this.altura = altura;
    }

    public String getNome() {
        return nome;
    }

    public double getPeso() {
        return peso;
    }

    public double getAltura() {
        return altura;
    }

    public double calcularIMC() {
        if (altura == 0) {
            throw new ArithmeticException("A altura não pode ser zero.");
        }

        return peso / (altura * altura);
    }

    public void mostrarDados() {
        System.out.printf(
            "Nome: %s | Peso: %.2f kg | Altura: %.2f m | IMC: %.2f%n",
            nome, peso, altura, calcularIMC()
        );
    }
}