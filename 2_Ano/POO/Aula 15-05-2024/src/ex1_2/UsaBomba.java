/*2. Crie uma classe chamada UsaBomba que utilize a classe do exercício anterior.
Ela deve conter o método main e:
- instanciar uma bomba (bomba1);
- ligar o objeto bomba1 durante 5 segundos; */

package ex1_2;

public class UsaBomba {
    public static void main(String[] args) {
        BombaDagua bomba1 = new BombaDagua(); // Instanciando uma bomba
        bomba1.ligar(5); // Ligando a bomba por 5 segundos
    }
}
