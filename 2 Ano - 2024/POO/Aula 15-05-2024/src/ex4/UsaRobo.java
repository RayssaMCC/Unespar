/*4. Crie uma interface chamada Controle que especifique os métodos "andar",
"virar" e "falar". A seguir, crie uma classe chamada Robo que implemente esses
métodos. Dentro de cada método imprima uma mensagem em tela contendo a
ação correspondente. Para testar, elabore uma terceira classe chamada
UsaRobo. */

package ex4;

// Interface Controle
interface Controle {
    void andar();
    void virar();
    void falar();
}

// Classe Robo que implementa a interface Controle
class Robo implements Controle {
    @Override
    public void andar() {
        System.out.println("O robô está andando.");
    }

    @Override
    public void virar() {
        System.out.println("O robô está virando.");
    }

    @Override
    public void falar() {
        System.out.println("O robô está falando.");
    }
}

// Classe UsaRobo para testar a funcionalidade do robô
public class UsaRobo {
    public static void main(String[] args) {
        Robo meuRobo = new Robo();

        // Testando os métodos do robô
        meuRobo.andar();
        meuRobo.virar();
        meuRobo.falar();
    }
}

