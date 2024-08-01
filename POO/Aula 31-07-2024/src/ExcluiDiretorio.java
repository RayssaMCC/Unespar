import java.io.File;
public class ExcluiDiretorio {
    public static void main(String[] args) {
        File dir = new File("C:/Users/rayss/OneDrive/Unespar/Disciplinas/POO/Aula 31-07-2024/loja");
        String men = "";
        if (dir.isDirectory()) {
            if (dir.delete ()) {
                men = dir.getName() + " Excluido com sucesso!";
            } else {
                if (excluirFilhos(dir)) {
                    men = dir.getName() + " Excluido com Sucesso!";
                } else {
                    men = "Falha na exclusao de " + dir.getName();
                }
            }
            System.out.println(men);
        }
    }

    private static boolean excluirFilhos(File dir) {
        if (dir.isDirectory()) {
            String[] arquivos = dir.list();
            for (int i = 0; i < arquivos.length; i++) {
                boolean success = excluirFilhos(new File(dir, 			arquivos[i]));
                if (success) {
                    System.out.println("Excluido: " + arquivos[i]);
                } else {
                    System.out.println("Nao pode ser excluido: " + arquivos[i]);
                    return false;
                }
            }
        }
        return dir.delete();
    }
}