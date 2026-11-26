package receitas;

public class Principal {

    public static void main(String[] args) {

        Receita[] receitas = {
            new BoloChocolate(),
            new Arroz(),
            new Lasanha()
        };

        Cardapio cardapio = new Cardapio(receitas);

        cardapio.mostrarCardapio();
    }
}
