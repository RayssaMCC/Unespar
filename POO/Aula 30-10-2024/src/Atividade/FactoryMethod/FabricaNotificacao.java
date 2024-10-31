package Atividade.FactoryMethod;

public abstract class FabricaNotificacao {
    public abstract Notificacao criarNotificacao();

    public void enviarNotificacao() {
        Notificacao notificacao = criarNotificacao();
        notificacao.notificarUsuario();
    }
}

