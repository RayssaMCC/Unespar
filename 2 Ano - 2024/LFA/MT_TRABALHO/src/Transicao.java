public class Transicao {
    private String direcao;
    private int estadoFuturo;
    private String alfabetoFuturo;

    //Construtor com parâmetros para inicializar uma nova instância de Transicao
    public Transicao(String direcao, int estadoFuturo, String alfabetoFuturo) {
        this.direcao = direcao;
        this.estadoFuturo = estadoFuturo;
        this.alfabetoFuturo = alfabetoFuturo;
    }

    //Construtor padrão vazio para permitir a criação de uma instância sem inicializar os campos
    public Transicao(){
        
    }

    //Método getter para obter o estado futuro
    public int getEstadoFuturo() {
        return estadoFuturo;
    }

    //Método setter para definir o estado futuro
    public void setEstadoFuturo (int estadoFuturo) {
        this.estadoFuturo = estadoFuturo;
    }

    //Método getter para obter o alfabeto futuro
    public String getAlfabetoFuturo() {
        return alfabetoFuturo;
    }

    //Método setter para definir o alfabeto futuro
    public void setAlfabetoFuturo(String alfabetoFuturo) {
        this.alfabetoFuturo = alfabetoFuturo;
    }

    //Método getter para obter a direção da transição
    public String getDirecao() {
        return direcao;
    }

    //Método setter para definir a direção da transição
    public void setDirecao(String direcao) {
        this.direcao = direcao;
    }
}