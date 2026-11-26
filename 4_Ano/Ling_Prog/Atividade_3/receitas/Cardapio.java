package receitas;

public class Cardapio {

    private Receita[] receitas;

    public Cardapio(Receita[] receitas) {
        this.receitas = receitas;
    }

    public void mostrarCardapio() {

        for (Receita receita : receitas) {

            System.out.println("\n===== RECEITA =====");
            System.out.println("Tipo: " + receita.getTipo());
            System.out.println("Ingredientes: "
                    + receita.getIngredientes());
            System.out.println("Modo de fazer: "
                    + receita.getModoDeFazer());

            if (receita instanceof Cozido) {
                ((Cozido) receita).cozinhar();
            }

            if (receita instanceof Assado) {
                ((Assado) receita).assar();
            }
        }
    }
}