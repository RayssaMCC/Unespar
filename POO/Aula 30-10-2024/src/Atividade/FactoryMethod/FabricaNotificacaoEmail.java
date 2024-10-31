package Atividade.FactoryMethod;

public class FabricaNotificacaoEmail extends FabricaNotificacao {
    @Override
    public Notificacao criarNotificacao() {
        return new NotificacaoEmail();
    }
}
