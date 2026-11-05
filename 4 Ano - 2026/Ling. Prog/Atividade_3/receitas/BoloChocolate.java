package receitas;

public class BoloChocolate extends Receita implements Assado {

    public BoloChocolate() {
        super("Doce");
    }

    @Override
    public String getIngredientes() {
        return "Farinha, açúcar, ovos, chocolate e leite.";
    }

    @Override
    public String getModoDeFazer() {
        return "Misture os ingredientes, coloque em uma forma "
             + "e leve ao forno.";
    }

    @Override
    public void assar() {
        System.out.println("O bolo de chocolate está assando.");
    }
}
