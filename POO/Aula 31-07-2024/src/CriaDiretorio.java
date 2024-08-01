import java.io.File;
public class CriaDiretorio {
    public static void main (String[] args) {
        File dir = new File("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024/loja");
        if (!dir.exists()) {
            dir.mkdir();
        }
        dir = new File("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024/loja/site");
        if (!dir.exists()) {
            dir.mkdir();
        }
        dir = new File("C:/Users/rayss//OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024/loja/site/imagens");
        if (!dir.exists()) {
            dir.mkdir();
        }
        dir = new File("C:/Users//rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024/loja/site/videos");
        if (!dir.exists()) {
            dir.mkdir();
        }
        dir = new File("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024/loja/site/sons");
        if (!dir.exists()) {
            dir.mkdir();
        }
        System.out.println("Final do processo de criaçao");
    }
}