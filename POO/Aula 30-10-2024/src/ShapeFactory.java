public class ShapeFactory {
    public Shape3D createShape(String shapeType) {
        switch (shapeType.toLowerCase()) {
            case "cilindro":
                return new Cilindro();
            case "esfera":
                return new Esfera();
            case "cubo":
                return new Cubo();
            case "tetraedro":
                return new Tetraedro();
            default:
                throw new IllegalArgumentException("Forma desconhecida: " + shapeType);
        }
    }
}