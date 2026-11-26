package nomes;

public class Main {
    public static void main(String[] args) {

        String s1 = "Programaçao";
        String s2 = "JAVA";
        String s3 = "java";

        //Concatenação de s1 com s2
        System.out.println("Concatenaçao: " + s1.concat(s2));

        //Tamanho das Strings s1 e s2
        System.out.println("Tamanho de s1: " + s1.length());
        System.out.println("Tamanho de s2: " + s2.length());

        //Primeiro caractere de s1 e s2 concatenados
        String primeirosCaracteres = String.valueOf(s1.charAt(0))
                .concat(String.valueOf(s2.charAt(0)));

        System.out.println("Primeiros caracteres concatenados: "
                + primeirosCaracteres);

        //Verificar se existe @ em s1
        System.out.println("Existe @ em s1? " + s1.contains("@"));

        //Inteiro 13 atribuído à String s2
        Integer numero = 13;
        s2 = String.valueOf(numero);

        System.out.println("Novo valor de s2: " + s2);
    }
}
