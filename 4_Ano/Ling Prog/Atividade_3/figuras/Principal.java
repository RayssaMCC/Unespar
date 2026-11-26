package figuras;

public class Principal {

    public static void main(String[] args) {

        FiguraGeometrica figura = new FiguraGeometrica();
        Circulo circulo = new Circulo();
        Quadrado quadrado = new Quadrado();
        Triangulo triangulo = new Triangulo();
        TrianguloEquilatero trianguloEquilatero = new TrianguloEquilatero();

        figura.desenha();
        circulo.desenha();
        quadrado.desenha();
        triangulo.desenha();
        trianguloEquilatero.desenha();
    }
}