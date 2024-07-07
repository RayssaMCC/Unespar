package mt_rissati;

import java.util.HashMap;

public class Estados {
    private boolean estado_final = false;
    //Dentro do objeto Estados, ele tera um hashmap com as transições referentes a este estado.
    //a cada nova instancia de estado sera colocado dentro do hashmap com a key da letra que ele precisara para fazer a transição.
    private HashMap<String, Transicao> transitions = new HashMap<>();

    public Estados(boolean estado_final){
        this.estado_final = estado_final;
    }

    public void setEstado_final(boolean estado_final){
        this.estado_final = estado_final;
    }

    public boolean getEstado_final(){
        return this.estado_final;
    }

    /**
     * O método {@code setTransicao()} recebera todos as informações para a criação de uma transição
     * onde o {@code letra_atual} sera a {@code key} do hashmap e as demais variaveis
     * {@code letra_futura}, {@code direcao}, {@code estado_futuro}. Serão utilizadas para
     * instanciar um novo objeto de {@code Transicao}.
     */
    public void setTransicao(String letra_atual, String letra_futura, String direcao, int estado_futuro){
        Transicao transition = new Transicao(direcao, estado_futuro, letra_futura);
        this.transitions.put(letra_atual, transition);
    }

    /**
     * O método {@code getTransicao()} recebera a letra do indice da fita sendo executada, e retornara
     * todas as informações armazenadas no objeto {@code Transicao}. Utilizando como parametro {@code letra_atual}
     * que sera a {@code key} para resgatar esses dados do HashMap.
     */
    public Transicao getTransicao(String letra_atual){
        return this.transitions.get(letra_atual);
    }
}
