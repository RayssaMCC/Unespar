https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html


public class ExemplosString {
    public static void main(String args[]) {
        String str = "Hello World";
        System.out.println(str.charAt(6));
        System.out.println("aab".compareTo("aab"));
        System.out.println("aaa" + "bbb");
        System.out.println(str.contains("Java"));
        System.out.println("imagem.png".endsWith(".exe"));
        System.out.println(str.hashCode());
        System.out.println(str.indexOf("llo"));
        System.out.println(" ".isBlank());
        System.out.println(" ".isEmpty());
        System.out.println(str.length());
        System.out.println(str.repeat(5));
        System.out.println(str.replace(" ", " alguma coisa "));
        String arr[] = str.split(" ");
        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(str.startsWith("java"));
        System.out.println(str.substring(3, 7));
        char arr_chars[] = str.toCharArray();
        for(int i=0; i<arr_chars.length; i++) {
            System.out.println(arr_chars[i]);
        }
        System.out.println(str.toUpperCase());
        System.out.println(str.toLowerCase());
    }

}