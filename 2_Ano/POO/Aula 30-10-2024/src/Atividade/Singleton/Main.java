package Atividade.Singleton;

public class Main {
    public static void main(String[] args) {
        Configuracoes c = Configuracoes.getInstance();
        Configuracoes c2 = Configuracoes.getInstance();

        if(c == c2) {
            System.out.println("Singleton funcionando");
        } else {
            System.out.println("Singleton não funcionando");    
        }
    }
}