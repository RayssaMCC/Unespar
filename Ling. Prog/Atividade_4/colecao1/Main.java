package colecao1;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Iterator;

public class Main {

    public static void main(String[] args) {

        // Criando 5 objetos da classe Aluno
        Aluno aluno1 = new Aluno(
                1,
                "Ana",
                "99999-1111",
                "Rua A"
        );

        Aluno aluno2 = new Aluno(
                2,
                "Bruno",
                "99999-2222",
                "Rua B"
        );

        Aluno aluno3 = new Aluno(
                3,
                "Carlos",
                "99999-3333",
                "Rua C"
        );

        Aluno aluno4 = new Aluno(
                4,
                "Daniela",
                "99999-4444",
                "Rua D"
        );

        Aluno aluno5 = new Aluno(
                5,
                "Eduardo",
                "99999-5555",
                "Rua E"
        );


        // ArrayList com 6 objetos e duplicando um aluno
        ArrayList<Aluno> listaAlunos = new ArrayList<>();

        listaAlunos.add(aluno1);
        listaAlunos.add(aluno2);
        listaAlunos.add(aluno3);
        listaAlunos.add(aluno4);
        listaAlunos.add(aluno5);
        // Aluno duplicado
        listaAlunos.add(aluno3);


        //HashSet com os nomes dos alunos
        HashSet<String> nomesAlunos = new HashSet<>();

        nomesAlunos.add(aluno1.getNome());
        nomesAlunos.add(aluno2.getNome());
        nomesAlunos.add(aluno3.getNome());
        nomesAlunos.add(aluno4.getNome());
        nomesAlunos.add(aluno5.getNome());

        /*
        HashMap com 7 chaves e 5 alunos
        aluno1 -> 2 chaves
        aluno2 -> 2 chaves
        aluno3 -> 1 chave
        aluno4 -> 1 chave
        aluno5 -> 1 chave
        */
        HashMap<String, Aluno> mapaAlunos = new HashMap<>();

        mapaAlunos.put("A001", aluno1);
        mapaAlunos.put("A002", aluno2);
        mapaAlunos.put("A003", aluno3);
        mapaAlunos.put("A004", aluno4);
        mapaAlunos.put("A005", aluno5);

        // Duas chaves apontando para alunos que já estão no mapa
        mapaAlunos.put("A006", aluno1);
        mapaAlunos.put("A007", aluno2);


        // Imprimir ArrayList utilizando for
        System.out.println("===== ALUNOS DO ARRAYLIST =====");

        for (int i = 0; i < listaAlunos.size(); i++) {
            listaAlunos.get(i).imprimeDados();
        }


        // Imprimir HashSet utilizando Iterator
        System.out.println("===== NOMES DO HASHSET =====");

        Iterator<String> iterator = nomesAlunos.iterator();

        while (iterator.hasNext()) {
            String nome = iterator.next();
            System.out.println(nome);
        }


        //Imprimir HashMap (chave + dados do aluno)
        System.out.println("\n===== ALUNOS DO HASHMAP =====");

        for (String chave : mapaAlunos.keySet()) {
            System.out.println("Chave: " + chave);
            Aluno aluno = mapaAlunos.get(chave);
            aluno.imprimeDados();
        }
    }
}