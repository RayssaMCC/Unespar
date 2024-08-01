import java.io.File;
import javax.swing.JOptionPane;

public class ListaDiretorio {
    public static void main(String args[]) {
        String path = JOptionPane.showInputDialog("Forneça o caminho " + "do diretorio (utilize / entre os diretorios)");
        File dir = new File(path);
        if (dir.isDirectory()) {
            System.out.println("Conteudo do diretorio " + path);
            String s[] = dir.list();
            for (int i = 0; i < s.length; i++) {
                System.out.println(s[i]);
            }
        } else {
                System.out.println(path + " não é um diretorio valido");
            }
        }
}