package heranca2;

public class TestaTudo {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Ana", "123.456.789-00", "01/01/2000", "2021001");
        aluno.mostrarAluno();

        ChefeDepartamento chefe = new ChefeDepartamento("Carlos", "111.222.333-44", "01/01/1985", "2021003", "01/01/2021", 5500.0, "TI", "01/01/2022", 55.5);
        chefe.mostrarChefe();
    }
}