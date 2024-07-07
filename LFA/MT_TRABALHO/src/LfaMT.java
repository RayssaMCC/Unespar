

import java.util.*;

public class LfaMT {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Esta Maquina de Turing entra com uma quantidade (n) de um numero qualquer"
                + " e a saida e a quantidade n elevado ao quadrado (n*n). Digite o numero e a quantidade n: ");
        String alg = s.nextLine();
        int n = s.nextInt();
        int tamanho= (n*n)+2;
                
        String[] vetor= new String[tamanho];
        vetor[0]= "x";
        for (int i=1; i<vetor.length; i++) {
            vetor[i]= "&";
        }
        for (int i=1; i<=n; i++) {
            vetor[i]= alg;
        }
        int point = 0;
        int estado = 0;
        
        while (estado!=13){
            while (estado==0) {
                while ("x".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while ("B".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                if (alg.equals(vetor[point])){
                    vetor[point]= "A";
                    point++;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                } else if ("&".equals(vetor[point])){
                    point--;
                    estado=3;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }

            while (estado==1) {
                while (alg.equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while ("B".equals(vetor[point])) {  
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                if ("&".equals(vetor[point])){
                    vetor[point]= "B";
                    point--;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
        
            while (estado==2) {
                while (alg.equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while ("B".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                if ("A".equals(vetor[point])){
                    point++;
                    estado=0;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
        
            while (estado==3) {
                if ("x".equals(vetor[point])){
                    point--;
                    estado=13;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                } else if ("B".equals(vetor[point])){
                    vetor[point]= "&";
                    point--;
                    estado=4;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
        
            while (estado==4) {
                while ("B".equals(vetor[point])) {
                    point--;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);             
                }
                if ("A".equals(vetor[point])) {
                    point++;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                   System.out.println("estado: q" + estado);
                }
            }
            
            while (estado==5){
                if ("B".equals(vetor[point])){
                    vetor[point]="C";
                    point--;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                } else if ("&".equals(vetor[point])){
                    point--;
                    estado=12;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                } 
            }
            
            while (estado==6) {
                while ("A".equals(vetor[point])) {
                    vetor[point]=alg;
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while ("C".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                   System.out.println("estado: q" + estado);
                }
                if ("x".equals(vetor[point])){
                    point++;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                  System.out.println("estado: q" + estado);
                }
            }
            
            while (estado==7) {
                if (alg.equals(vetor[point])){
                    vetor[point]="A";
                    point++;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
            
            while (estado==8) {
                if (alg.equals(vetor[point])){
                    vetor[point]="A";
                    point++;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                } else if ("C".equals(vetor[point])) {
                    point++;
                    estado=11;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
            
            while (estado==9) {
                while ("C".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while ("B".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while (alg.equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                if ("&".equals(vetor[point])){
                    vetor[point]=alg;
                    point--;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
            
            while (estado==10) {
                while ("C".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while ("B".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while (alg.equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                if ("A".equals(vetor[point])){
                    point++;
                    estado=8;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
            
            while (estado==11) {
                while ("C".equals(vetor[point])) {
                    System.out.println(Arrays.toString(vetor));
                    point++;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                if ("B".equals(vetor[point])){
                    vetor[point]="C";
                    point--;
                    estado=6;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                } else if (alg.equals(vetor[point])) {
                    point--;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
            }
            
            while (estado==12) {
                while ("A".equals(vetor[point])) {
                    vetor[point]=alg;
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                while ("C".equals(vetor[point])) {
                    vetor[point]=alg;
                    System.out.println(Arrays.toString(vetor));
                    point--;
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                }
                if ("x".equals(vetor[point])){
                    point++;
                    estado++;
                    System.out.println(Arrays.toString(vetor));
                    System.out.println("ponteiro: " + point);
                    System.out.println("estado: q" + estado);
                } 
            }
        }
        s.close();
    }
}