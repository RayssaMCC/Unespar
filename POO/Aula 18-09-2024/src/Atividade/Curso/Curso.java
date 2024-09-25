package Atividade.Curso;
public class Curso {
    private int id;
    private String nome;
    private int duracao;
    private String descricao;

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

    public int getDuracao() {
        return duracao;
    }

    public void setDuracao(int duracao) {
        this.duracao = duracao;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    // Método para exibir informações do curso
    public String toString() {
        return "Curso [id=" + id + ", nome=" + nome + ", duracao=" + duracao + ", descricao=" + descricao + "]";
    }
}
