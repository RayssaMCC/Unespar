/* teste anterior à adição do código em C


import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class Bloco {
    int tamanhoTotal;
    int tamanhoAlocado;
    boolean ocupado;

    Bloco(int tamanhoTotal) {
        this.tamanhoTotal = tamanhoTotal;
        this.tamanhoAlocado = 0;
        this.ocupado = false;
    }

    void alocar(int tamanho) {
        if (tamanho <= tamanhoDisponivel()) {
            this.tamanhoAlocado += tamanho;
            this.ocupado = tamanhoAlocado == tamanhoTotal;
        }
    }

    void liberar(int tamanho) {
        if (tamanho <= this.tamanhoAlocado) {
            this.tamanhoAlocado -= tamanho;
            this.ocupado = false;
        }
    }

    int tamanhoDisponivel() {
        return tamanhoTotal - tamanhoAlocado;
    }

    @Override
    public String toString() {
        if (ocupado) {
            return "[" + tamanhoTotal + " total, " + tamanhoAlocado + " alocado, ocupado]";
        } else {
            return "[" + tamanhoTotal + " total, " + tamanhoAlocado + " alocado, livre]";
        }
    }

    public static class SimuladorDeAlocacao {
        private List<Bloco> memoria;

        public SimuladorDeAlocacao() {
            memoria = new ArrayList<>();
            memoria.add(new Bloco(100));
            memoria.add(new Bloco(500));
            memoria.add(new Bloco(200));
            memoria.add(new Bloco(300));
            memoria.add(new Bloco(600));
        }

        public void alocarEspaco(int tamanho, String tipoAjuste) {
            switch (tipoAjuste) {
                case "A":
                    primeiroAjuste(tamanho);
                    break;
                case "M":
                    melhorAjuste(tamanho);
                    break;
                case "P":
                    piorAjuste(tamanho);
                    break;
                default:
                    System.out.println("Tipo de ajuste desconhecido.");
                    break;
            }
        }

        public void primeiroAjuste(int tamanho) {
            for (Bloco bloco : memoria) {
                if (bloco.tamanhoDisponivel() >= tamanho) {
                    bloco.alocar(tamanho);
                    System.out.println("Primeiro Ajuste: Alocado " + tamanho);
                    return;
                }
            }
            System.out.println("Primeiro Ajuste: Nao foi possivel alocar " + tamanho);
        }

        public void melhorAjuste(int tamanho) {
            memoria.sort(Comparator.comparingInt(Bloco::tamanhoDisponivel));
            for (Bloco bloco : memoria) {
                if (bloco.tamanhoDisponivel() >= tamanho) {
                    bloco.alocar(tamanho);
                    System.out.println("Melhor Ajuste: Alocado " + tamanho);
                    return;
                }
            }
            System.out.println("Melhor Ajuste: Nao foi possivel alocar " + tamanho);
        }

        public void piorAjuste(int tamanho) {
            memoria.sort((b1, b2) -> b2.tamanhoDisponivel() - b1.tamanhoDisponivel());
            for (Bloco bloco : memoria) {
                if (bloco.tamanhoDisponivel() >= tamanho) {
                    bloco.alocar(tamanho);
                    System.out.println("Pior Ajuste: Alocado " + tamanho);
                    return;
                }
            }
            System.out.println("Pior Ajuste: Nao foi possivel alocar " + tamanho);
        }
        
        public void liberarEspaco(int tamanho) {
            for (Bloco bloco : memoria) {
                if (bloco.tamanhoAlocado == tamanho) {
                    bloco.liberar(tamanho);
                    System.out.println("Espaco de " + tamanho + " liberado.");
                    return;
                }
            }
            System.out.println("Nao foi possivel liberar espaco de " + tamanho);
        }

        public void mostrarMemoria() {
            memoria.forEach(System.out::println);
        }

        public static void main(String[] args) {
            SimuladorDeAlocacao simulador = new SimuladorDeAlocacao();
            Scanner sc = new Scanner(System.in);

            System.out.println("Digite (A) para primeiro ajuste, (M) para melhor ajuste ou (P) para pior ajuste:");
            String tipoAjuste = sc.next().toUpperCase();

            while (true) {
                System.out.println("Digite (A) para alocar, (L) para liberar ou (X) para sair:");
                String comando = sc.next().toUpperCase();
                if (comando.equals("X")) {
                    break;
                }
                System.out.println("Digite a quantidade de KB:");
                int tamanho = sc.nextInt();

                switch (comando) {
                    case "A":
                        simulador.alocarEspaco(tamanho, tipoAjuste);
                        break;
                    case "L":
                        simulador.liberarEspaco(tamanho);
                        break;
                    default:
                        System.out.println("Comando desconhecido.");
                        break;
                }
                simulador.mostrarMemoria();
            }
            sc.close();
        }
    }
} */