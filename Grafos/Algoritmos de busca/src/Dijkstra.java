//Implementação do algoritmo de Dijkstra para encontrar as menores distâncias em um grafo

import java.util.*;

public class Dijkstra{
    public class No{
        private String node;
        private Map<No, Integer> vizinhos; //mapa que armazena os vizinhos e os pesos das arestas

        public No(String node){ //inicializa nó e mapa de vizinhos
            this.node = node;
            this.vizinhos = new HashMap<>();
        }

        public String getNode(){ 
            return node;
        }

        public Map<No, Integer> getVizinhos(){
            return vizinhos;
        }

        public void adicionarVizinho(No vizinho, int peso){ //adiciona vizinhos e pesos no mapa
            this.vizinhos.put(vizinho, peso);
        }
    }

    //Implementação do Dijkstra
    public void dijkstra(No inicio){
        Map<No, Integer> distancias = new HashMap<>(); //armazena a menor distância conhecida até cada nó
        PriorityQueue<NoDistancia> fila = new PriorityQueue<>(Comparator.comparingInt(NoDistancia::getDistancia)); //fila de prioridade ordenada pela menor distância
        Set<No> visitados = new HashSet<>(); //rastreia os nós visitados 

        //nó de inicio tem distância 0 e é adicionado na fila
        distancias.put(inicio, 0);
        fila.add(new NoDistancia(inicio, 0));

        //enquanto houver nós na fila de prioridade
        while (!fila.isEmpty()){
            NoDistancia atual = fila.poll(); //remove o nó com a menor distância
            No noAtual = atual.getNo();
 
            if (visitados.contains(noAtual)) continue; //ignora se o nó já foi visitado
            visitados.add(noAtual); //senão marca como visitado

            //explora os vizinhos do nó atual
            for (Map.Entry<No, Integer> entrada : noAtual.getVizinhos().entrySet()){
                No vizinho = entrada.getKey(); //obtém o vizinho
                int peso = entrada.getValue(); //obtém o peso da aresta que conecta o nó atual ao vizinho

                //obtém a menor distância conhecida até o vizinho
                int novaDistancia = distancias.getOrDefault(noAtual, Integer.MAX_VALUE) + peso; //se o nó não foi visitado, a distância é infinita
                
                //se uma nova distância for menor que a conhecida, atualiza
                if (novaDistancia < distancias.getOrDefault(vizinho, Integer.MAX_VALUE)){
                    distancias.put(vizinho, novaDistancia);
                    fila.add(new NoDistancia(vizinho, novaDistancia)); //adiciona o vizinho na fila com a nova menor distância
                }
            }
        }

        //exibe as distâncias mínimas a partir do nó de início
        System.out.println("Distâncias mínimas a partir de " + inicio.getNode() + ":");
        for (Map.Entry<No, Integer> entry : distancias.entrySet()){
            System.out.println("Até " + entry.getKey().getNode() + ": " + entry.getValue());
        }
    }

    //classe auxiliar para armazenar um nó e sua distância
    public class NoDistancia{
        private No no;
        private int distancia;

        public NoDistancia(No no, int distancia){
            this.no = no;
            this.distancia = distancia;
        }

        public No getNo(){
            return no;
        }

        public int getDistancia(){
            return distancia;
        }
    }
}
