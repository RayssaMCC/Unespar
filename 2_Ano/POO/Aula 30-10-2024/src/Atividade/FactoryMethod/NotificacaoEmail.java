package Atividade.FactoryMethod;

public class NotificacaoEmail implements Notificacao {
    @Override
    public void notificarUsuario() {
        System.out.println("Enviando uma notificaçao por Email.");
    }
}
