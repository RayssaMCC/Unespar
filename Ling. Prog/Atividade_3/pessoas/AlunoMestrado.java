package pessoas;

public class AlunoMestrado extends Aluno {

    private Double conceitoDissertacao;
    private Double notaDissertacao;

    public Double getConceitoDissertacao() {
        return conceitoDissertacao;
    }

    public void setConceitoDissertacao(Double conceitoDissertacao) {
        this.conceitoDissertacao = conceitoDissertacao;
    }

    public Double getNotaDissertacao() {
        return notaDissertacao;
    }

    public void setNotaDissertacao(Double notaDissertacao) {
        this.notaDissertacao = notaDissertacao;
    }

    public Boolean aprovado() {
        return conceitoDissertacao >= 7.0
                && notaDissertacao >= 7.0
                && getMedia() >= 7.0;
    }

    @Override
    public void imprimeDados() {
        super.imprimeDados();

        System.out.println("Conceito da dissertaçao: " + conceitoDissertacao);
        System.out.println("Nota da dissertaçao: " + notaDissertacao);
    }
}
