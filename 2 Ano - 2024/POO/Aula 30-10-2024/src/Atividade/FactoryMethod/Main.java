package Atividade.FactoryMethod;

public class Main {
    public static void main(String[] args) {
        FabricaNotificacao fabricaEmail = new FabricaNotificacaoEmail();
        fabricaEmail.enviarNotificacao();

        FabricaNotificacao fabricaSMS = new FabricaNotificacaoSMS();
        fabricaSMS.enviarNotificacao();
    }
}
