//Implementação da interface "Cor"
interface Color {
    void applyColor();
}

//Implementação concreta para "vermelho"
class RedColor implements Color {
    public void applyColor() {
        System.out.println("cor vermelha aplicada.");
    }
}

//Implementação concreta para "azul"
class BlueColor implements Color {
    public void applyColor() {
        System.out.println("cor azul aplicada.");
    }
}

//Abstração "Forma"
abstract class Shape {
    protected Color color;

    public Shape(Color color) {
        this.color = color;
    }

    abstract void draw();
}

//Implementação concreta para "Círculo"
class Circle extends Shape {
    public Circle(Color color) {
        super(color);
    }

    public void draw() {
        System.out.print("Desenhando um círculo com ");
        color.applyColor();
    }
}

//Implementação concreta para "Quadrado"
class Square extends Shape {
    public Square(Color color) {
        super(color);
    }

    public void draw() {
        System.out.print("Desenhando um quadrado com ");
        color.applyColor();
    }
}

//Classe de teste
public class PadraoBridge {
    public static void main(String[] args) {
        Shape redCircle = new Circle(new RedColor());
        Shape blueCircle = new Circle(new BlueColor());
        Shape blueSquare = new Square(new BlueColor());
        Shape redSquare = new Square(new RedColor());

        redCircle.draw();
        blueCircle.draw();
        blueSquare.draw();
        redSquare.draw();
        
    }
}
