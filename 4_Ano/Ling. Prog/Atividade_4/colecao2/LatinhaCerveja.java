package colecao2;

public class LatinhaCerveja {

    private int id;
    private String marca;
    private int conteudo;
    private String fabricacao;
    private String validade;

    // Construtor
    public LatinhaCerveja(int id, String marca, int conteudo,
                          String fabricacao, String validade) {
        this.id = id;
        this.marca = marca;
        this.conteudo = conteudo;
        this.fabricacao = fabricacao;
        this.validade = validade;
    }

    // Método para imprimir os dados
    public void imprimeDados() {
        System.out.println("ID: " + id);
        System.out.println("Marca: " + marca);
        System.out.println("Conteúdo: " + conteudo + " ml");
        System.out.println("Fabricaçao: " + fabricacao);
        System.out.println("Data de validade: " + validade);
        System.out.println("----------------------------");
    }
}