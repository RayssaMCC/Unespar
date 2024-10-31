package Atividade.FactoryMethod;

public class NotificacaoSMS implements Notificacao {
    @Override
    public void notificarUsuario() {
        System.out.println("Enviando uma notificaçao por SMS.");
    }
}

