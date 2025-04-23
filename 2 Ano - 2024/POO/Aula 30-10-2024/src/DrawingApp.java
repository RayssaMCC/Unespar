import java.util.Scanner;

public class DrawingApp {
    public static void main(String[] args) {
        DrawingConfiguration config = DrawingConfiguration.getInstance();
        config.showConfig();

        ShapeFactory factory = new ShapeFactory();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha uma forma para desenhar (cilindro, esfera, cubo, tetraedro): ");
        String shapeType = scanner.nextLine();

        try {
            Shape3D shape = factory.createShape(shapeType);
            shape.draw();
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        } finally {
            scanner.close();
        }
    }
}