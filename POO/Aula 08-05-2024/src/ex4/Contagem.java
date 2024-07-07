/*Crie uma classe chamada Contagem que contenha quatro métodos com o nome “contar”
utilizando o conceito da sobrecarga. A assinatura e função de cada método aparecem descritas
na tabela a seguir. Faça também outra classe para testar o método. */

package ex4;

public class Contagem {
    public void contar() {
        for (int i = 0; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public void contar(int fim) {
        for (int i = 0; i <= fim; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public void contar(int inicio, int fim) {
        for (int i = inicio; i <= fim; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public void contar(int inicio, int fim, int pausa) {
        for (int i = inicio; i <= fim; i++) {
            System.out.print(i + " ");
            try {
                Thread.sleep(pausa * 1000); // Convertendo segundos para milissegundos
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println();
    }
}
