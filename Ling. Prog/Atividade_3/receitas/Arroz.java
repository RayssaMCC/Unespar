package receitas;

public class Arroz extends Receita implements Cozido {

    public Arroz() {
        super("Salgado");
    }

    @Override
    public String getIngredientes() {
        return "Arroz, água, óleo, alho e sal.";
    }

    @Override
    public String getModoDeFazer() {
        return "Refogue o alho, acrescente o arroz e a água "
             + "e cozinhe até ficar pronto.";
    }

    @Override
    public void cozinhar() {
        System.out.println("O arroz está cozinhando.");
    }
}
