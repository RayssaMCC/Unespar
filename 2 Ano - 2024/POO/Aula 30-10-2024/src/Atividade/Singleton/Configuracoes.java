package Atividade.Singleton;

public class Configuracoes {

    private static Configuracoes instance;

    private Configuracoes(){

    }

    public static Configuracoes getInstance(){
        if(instance == null){
            synchronized (Configuracoes.class){
                if(instance == null){
                    instance = new Configuracoes();
                }
            }
        }
        return instance;
    } 
}
