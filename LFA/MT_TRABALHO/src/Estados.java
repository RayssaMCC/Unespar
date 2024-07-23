import java.util.HashMap;

public class Estados {
    private boolean estadoFinal = false; //Variavel que define se o estado é final ou não
    
    //HashMap para armazenar as transições. A chave é uma String representando a letra atual, e o valor é um objeto Transicao que contém os detalhes da transição
    private HashMap<String, Transicao> transicoes = new HashMap<>();

    //Construtor que permite definir se o estado é final no momento da criação do objeto Estados
    public Estados(boolean estadoFinal){
        this.estadoFinal = estadoFinal;
    }

    // Setter para alterar o valor de estadoFinal após a criação do objeto
    public void setEstadoFinal(boolean estadoFinal){
        this.estadoFinal = estadoFinal;
    }

    //Getter para verificar se o estado é final
    public boolean getEstadoFinal(){
        return this.estadoFinal;
    }
    
    //Método para adicionar uma nova transição ao estado
    //Recebe a letra atual como chave do HashMap e os detalhes da transição (letraFutura, direcao, estadoFuturo) para criar um novo objeto Transicao e armazená-lo no HashMap
    public void setTransicao(String letraAtual, String letraFutura, String direcao, int estadoFuturo){
        Transicao transicao = new Transicao(direcao, estadoFuturo, letraFutura);
        this.transicoes.put(letraAtual, transicao);
    }

    //Método para obter uma transição baseada na letra atual. Usa a letraAtual como chave para buscar no HashMap e retornar o objeto Transicao correspondente
    public Transicao getTransicao(String letraAtual){
        return this.transicoes.get(letraAtual);
    }
}
