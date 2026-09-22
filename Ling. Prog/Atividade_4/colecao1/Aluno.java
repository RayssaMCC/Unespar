package colecao1;

public class Aluno {

    private int codigo;
    private String nome;
    private String telefone;
    private String endereco;

    // Construtor
    public Aluno(int codigo, String nome, String telefone, String endereco) {
        this.codigo = codigo;
        this.nome = nome;
        this.telefone = telefone;
        this.endereco = endereco;
    }

    // Método para imprimir os dados
    public void imprimeDados() {
        System.out.println("Código: " + codigo);
        System.out.println("Nome: " + nome);
        System.out.println("Telefone: " + telefone);
        System.out.println("Endereço: " + endereco);
        System.out.println("----------------------------");
    }

    // Getter do nome
    public String getNome() {
        return nome;
    }
}