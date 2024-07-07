/*1. Faça uma classe que simule o funcionamento de uma bomba d ́água. A bomba
possui um atributo booleano chamado “status” e os métodos “ligar” e “desligar”
(ambos sem retorno). O método “ligar" coloca true em "status" e o método
"desligar" coloca false em status. A bomba deve ficar ligada durante um certo
intervalo de tempo (10 segundos). O tempo em segundos deve ser recebido pelo
método ligar. A cada segundo, apresente em tela quantos segundos faltam para a
bomba ser desligada. Decorrido o tempo, o método desligar é acionado e a bomba
é desligada. */

package ex1_2;

public class BombaDagua {
    private boolean status;

    public void ligar(int tempo) {
        status = true;
        System.out.println("Bomba ligada por " + tempo + " segundos.");
        for (int i = tempo; i > 0; i--) {
            System.out.printf("\nBomba ligada. Tempo restante: %d", i);
            try {
                Thread.sleep(1000); // Aguarda 1 segundo
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        desligar();
    }

    public void desligar() {
        status = false;
        System.out.println("\nBomba desligada.");
    }

    public static void main(String[] args) {
        BombaDagua bomba = new BombaDagua();
        bomba.ligar(10); // Ligar a bomba por 10 segundos
    }
}
