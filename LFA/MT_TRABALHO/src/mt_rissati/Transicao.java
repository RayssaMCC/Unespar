package mt_rissati;
public class Transicao {
    private String direction;
    private int estado_futuro;
    private String alfabeto_futuro;

    public Transicao(String direction, int estado_futuro, String alfabeto_futuro) {
        this.direction = direction;
        this.estado_futuro = estado_futuro;
        this.alfabeto_futuro = alfabeto_futuro;
    }

    public Transicao(){
        
    }

    public int getEstado_futuro() {
        return estado_futuro;
    }

    public void setEstado_futuro (int estado_futuro) {
        this.estado_futuro = estado_futuro;
    }

    public String getAlfabeto_futuro() {
        return alfabeto_futuro;
    }

    public void setAlfabeto_futuro(String alfabeto_futuro) {
        this.alfabeto_futuro = alfabeto_futuro;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
}
