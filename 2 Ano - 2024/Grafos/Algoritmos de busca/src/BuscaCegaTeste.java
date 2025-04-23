//Implementação dos algoritmos de busca cega (profundidade e largura)

import java.util.*;

public class BuscaCegaTeste{
    public class No{
        private String node;
        private List<No> vizinhos;

        public No(String node){ //inicializa nó e lista de vizinhos
            this.node = node;
            this.vizinhos = new ArrayList<>();
        }

        public String getNode(){ //função para retornar o nó
            return node;
        }

        public List<No> getVizinhos(){ //função para retornar vizinhos
            return vizinhos;
        }

        public void adicionarVizinho(No vizinho){ //função para adicionar vizinhos
            this.vizinhos.add(vizinho);
        }
    }

    //Busca em profundidade (DFS)
    public void profundidade(No raiz){
        Set<No> visitados = new HashSet<>(); //rastreia os nós visitados (evita visitar o mesmo nó mais de uma vez)
        Stack<No> pilha = new Stack<>(); //pilha para controlar a ordem de visita dos nós
        pilha.push(raiz); //adiciona o nó raiz na pilha

        while(!pilha.isEmpty()){ //enquanto tiver nó na pilha
            No atual = pilha.pop(); //tira o nó do topo da pilha

            if(!visitados.contains(atual)){ //se o nó não foi visitado
                visitados.add(atual); //marca o nó como visitado

                System.out.println("Visitando: " + atual.getNode());

                List<No> vizinhos = atual.getVizinhos(); 
                for (int i = vizinhos.size() - 1; i >= 0; i--){ //percorre os vizinhos de forma inversa para manter a ordem correta na pilha
                    pilha.push(vizinhos.get(i));
                }
            }
        }
    }

    //Busca em largura (BFS)
    public void largura(No raiz){
        Set<No> visitados = new HashSet<>();
        Queue<No> fila = new LinkedList<>(); //fila para controlar a ordem de visita dos nós
        fila.add(raiz); //adiciona o nó raiz na fila

        while(!fila.isEmpty()){ //enquanto tiver nó na fila
            No atual = fila.poll(); //retira o nó da frente da fila

            if(!visitados.contains(atual)){ //se o nó não foi visitado
                visitados.add(atual); //marca o nó como visitado

                System.out.println("Visitando: " + atual.getNode());

                for(No vizinho : atual.getVizinhos()){ //percorre os vizinhos do nó atual
                    fila.add(vizinho); //adiciona o vizinho na fila
                }
            }
        }
    }

    public static void main(String[] args) {
        BuscaCega buscas = new BuscaCega();

        BuscaCega.No noA = buscas.new No("A");
        BuscaCega.No noB = buscas.new No("B");
        BuscaCega.No noC = buscas.new No("C");
        BuscaCega.No noD = buscas.new No("D");
        BuscaCega.No noE = buscas.new No("E");
        BuscaCega.No noF = buscas.new No("F");
        BuscaCega.No noG = buscas.new No("G");
        BuscaCega.No noH = buscas.new No("H");
        BuscaCega.No noI = buscas.new No("I");
        BuscaCega.No noJ = buscas.new No("J");
        BuscaCega.No noK = buscas.new No("K");
        BuscaCega.No noL = buscas.new No("L");
        BuscaCega.No noM = buscas.new No("M");

        noA.adicionarVizinho(noB);
        noA.adicionarVizinho(noC);
        noA.adicionarVizinho(noD);
        noB.adicionarVizinho(noE);
        noB.adicionarVizinho(noF);
        noE.adicionarVizinho(noJ);
        noE.adicionarVizinho(noK);
        noC.adicionarVizinho(noG);
        noC.adicionarVizinho(noH);
        noD.adicionarVizinho(noI);
        noG.adicionarVizinho(noL);
        noL.adicionarVizinho(noM);

        System.out.println("Busca em Profundidade:");
        buscas.profundidade(noA);

        System.out.println("\nBusca em Largura:");
        buscas.largura(noA);
    }
}