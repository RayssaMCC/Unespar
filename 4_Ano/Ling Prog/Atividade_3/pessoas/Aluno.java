package pessoas;

public class Aluno extends Pessoa {

    private int numMatricula;
    private Double media;
    private int faltas;

    public int getNumMatricula() {
        return numMatricula;
    }

    public void setNumMatricula(int numMatricula) {
        this.numMatricula = numMatricula;
    }

    public Double getMedia() {
        return media;
    }

    public void setMedia(Double media) {
        this.media = media;
    }

    public int getFaltas() {
        return faltas;
    }

    public void setFaltas(int faltas) {
        this.faltas = faltas;
    }

    @Override
    public void imprimeDados() {
        super.imprimeDados();

        System.out.println("Número da matrícula: " + numMatricula);
        System.out.println("Média: " + media);
        System.out.println("Faltas: " + faltas);
    }
}
