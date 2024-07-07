import java.util.*;

public class Raids {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        //Inicialização dos discos
        ArrayList<Character> disco1 = new ArrayList<>();
        ArrayList<Character> disco2 = new ArrayList<>();
        ArrayList<Character> disco3 = new ArrayList<>();
        ArrayList<Character> discoParidade = new ArrayList<>();

        System.out.printf("Informe a frase para os RAIDs: ");
        String frase = sc.nextLine();

        //RAID 0
        System.out.println("RAID 0");
        //Distribuição das letras pelos discos
        for (int i = 0; i < frase.length(); i++) {
            if (i % 2 == 0) {
                disco1.add(frase.charAt(i)); //Par adiciona ao disco 1
            } 
            else if (i % 2 != 0) {
                disco2.add(frase.charAt(i)); //Impar adiciona ao disco 2
            }
        }

        //Imprime os discos
        System.out.printf("Disco 1: ");
        for (Character c : disco1) {
            System.out.print(c);
        }

        System.out.printf("\nDisco 2: ");
        for (Character c : disco2) {
            System.out.print(c);
        }

        //RAID 1
        System.out.println("\n\nRAID 1");
        System.out.println("Disco 1: " + frase);
        System.out.println("Disco 2 (backup): " + frase);

        //Limpeza dos discos para o RAID 4
        disco1.clear();
        disco2.clear();
        disco3.clear();

        //RAID 4
        System.out.println("\nRAID 4");
        //Distribuição das letras pelos discos
        for (int i = 0; i < frase.length(); i++) {
            if (i % 3 == 0){ //Divisível por 3 adiciona ao disco 1
                disco1.add(frase.charAt(i)); 
            } 
            else if (i % 3 == 1) { //Se não for divisível por 3
                disco2.add(frase.charAt(i)); //Adiciona ao disco 2
            }
            else { 
                disco3.add(frase.charAt(i)); //Adiciona ao disco 3
            } 
        }
        
        //Cálculo do disco de paridade para RAID 4
        for (int i = 0; i < frase.length(); i++) {
            char paridade = 0;
            if (i < disco1.size()) {
                paridade ^= disco1.get(i);
            }
            if (i < disco2.size()) {
                paridade ^= disco2.get(i);
            }
            if (i < disco3.size()) {
                paridade ^= disco3.get(i);
            }
            discoParidade.add(paridade); //Adiciona o resultado da paridade ao disco de paridade
        }

        //Imprime os discos de RAID 4
        System.out.printf("Disco 1: ");
        for (Character c : disco1) {
            System.out.print(c);
        }
        System.out.printf("\nDisco 2: ");
        for (Character c : disco2) {
            System.out.print(c);
        }
        System.out.printf("\nDisco 3: ");
        for (Character c : disco3) {
            System.out.print(c);
        }
        System.out.printf("\nDisco de Paridade: ");
        for (Character c : discoParidade) {
            System.out.print(c);
        }

        //Simulação da remoção do disco 3 e recuperação dos dados
        System.out.println("\n\nSimulacao da remocao do disco 3 e recuperacao dos dados:");
        ArrayList<Character> discoRecuperado = new ArrayList<>();
        for (int i = 0; i < discoParidade.size(); i++) {
            char dadoRecuperado = discoParidade.get(i); //Começa com o valor da paridade
            if (i < disco1.size()) {
                dadoRecuperado ^= disco1.get(i); //Aplica XOR com o disco 1
            }
            if (i < disco2.size()) {
                dadoRecuperado ^= disco2.get(i); //Aplica XOR com o disco 2
            }
            discoRecuperado.add(dadoRecuperado); //Adiciona o resultado ao disco recuperado
        }

        //Imprime os discos restantes e o recuperado
        System.out.printf("Disco 1: ");
        for (Character c : disco1) {
            System.out.print(c);
        }
        System.out.printf("\nDisco 2: ");
        for (Character c : disco2) {
            System.out.print(c);
        }
        System.out.printf("\nDisco de Paridade: ");
        for (Character c : discoParidade) {
            System.out.print(c);
        }
        System.out.printf("\nDisco 3 recuperado: ");
        for (Character c : discoRecuperado) {
            System.out.print(c);
        }
        
        sc.close();
    }
}