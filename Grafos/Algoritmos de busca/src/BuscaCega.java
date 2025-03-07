//Implementação dos algoritmos de busca cega (profundidade e largura)

import java.util.*;

public class BuscaCega{
    public class No{
        private String node;
        private List<No> vizinhos; //lista que armazena os vizinhos

        public No(String node){ //inicializa nó e lista de vizinhos
            this.node = node;
            this.vizinhos = new ArrayList<>();
        }

        public String getNode(){
            return node;
        }

        public List<No> getVizinhos(){
            return vizinhos;
        }

        public void adicionarVizinho(No vizinho){ //adiciona vizinhos na lista
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
                    pilha.push(vizinhos.get(i)); //adiciona o vizinho na pilha
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
}