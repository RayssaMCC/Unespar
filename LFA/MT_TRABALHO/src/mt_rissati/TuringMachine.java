package mt_rissati;
import java.util.Scanner;
import java.util.HashMap;

public class TuringMachine{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int quant_letras_alfabeto;
        System.out.println("Informe a quantidade de letras do alfabeto");
        quant_letras_alfabeto = Integer.parseInt(scan.nextLine());

        String letras_alfabeto[] = new String[quant_letras_alfabeto];
        for(int i = 0; i < quant_letras_alfabeto; i++){
            System.out.println("informe uma letra do alfabeto");
            letras_alfabeto[i] = scan.nextLine();
        }

        System.out.println("Digite a quantidade de letras do alfabeto auxiliar");
        int quant_letras_alfabeto_auxiliar;
        quant_letras_alfabeto_auxiliar = Integer.parseInt(scan.nextLine());

        String letras_alfabeto_auxiliar[] = new String[quant_letras_alfabeto_auxiliar];
        for(int i = 0; i < quant_letras_alfabeto_auxiliar; i++){
            System.out.println("Informe uma letra do alfabeto auxiliar:");
            letras_alfabeto_auxiliar[i] = scan.nextLine();
        }

        int quant_estados;
        System.out.println("informe a quantidade de estados:");
        quant_estados = Integer.parseInt(scan.nextLine());
        

        System.out.println("Informe o estado inicial:");
        int estado_inicial = Integer.parseInt(scan.nextLine());

        System.out.println("Informe a quantidade de estados finais:");
        int quant_estados_finais = Integer.parseInt(scan.nextLine());

        int estado_final[] = new int[quant_estados_finais];
        for(int i = 0; i < quant_estados_finais; i++){
            System.out.println("Informe um estado final:");
            estado_final[i] = Integer.parseInt(scan.nextLine());
        }

        System.out.println("informe o marcador de inicio:");
        String marca_inicio = scan.nextLine();

        System.out.println("informe o marcador para branco");
        String marca_branco = scan.nextLine();

        System.out.println("Entre a palavra a ser testada: ");
        //palavra enserida pelo usuario que vai ser alocada na fita principal
        String palavra[] = scan.nextLine().split("");

        //Cria a variavel da fita principal e chama o método alocarFita () que ira colocar ela com marcador de inicio na primeira posição, 
        //e o resto da array é preenchido com o marcador branco.
        String fita[] = new String[100];
        alocarFita(fita, palavra, marca_inicio, marca_branco);
        
        //inicio das informações sobre a tabela de transição
        //Esta estrura de repetição apenas fara papel de visualização, ela mostra uma array de 2 dimensões montada apenas para 
        //guiar o usuario em qual lugar esta o espaço de cada transição.
        //int tabela_transi[][] = new int[quant_estados][quant_letras_alfabeto_auxiliar + quant_letras_alfabeto + 2];
        System.out.println();
        System.out.println("===== TABELA DE TRANSIÇÃO =====");
        System.out.print("   ");
        for(String i : letras_alfabeto){
            System.out.print(i + "   ");
        }
        for(String i : letras_alfabeto_auxiliar){
            System.out.print(i + "   ");
        }
        System.out.print(marca_inicio + "   " + marca_branco + "\n");
        for(int i = 1; i < quant_estados + 1; i++){
            System.out.print("S" + i + " ");
            for(int j = 1; j < (quant_letras_alfabeto + quant_letras_alfabeto_auxiliar + 1 + 2); j++){
                System.out.print( i +","+ j + " ");
            }
            System.out.println();
        }

        //HashMap que sera usado pra salvar os Estados presentes na execução dada pelo usuario.
        HashMap<Integer, Estados> mapEstados = new HashMap<>();

        //Array que armazena todos os alfabetos que servira como passagem de paramentro pra instancia de uma transição
        //dentro dos estados.
        String alfabeto_geral[] = new String[quant_letras_alfabeto + quant_letras_alfabeto_auxiliar + 2];
        int indice_auxiliar_alfabeto_geral = 0;
        while(indice_auxiliar_alfabeto_geral < alfabeto_geral.length){
            for(String i : letras_alfabeto){
                alfabeto_geral[indice_auxiliar_alfabeto_geral] = i;
                indice_auxiliar_alfabeto_geral++;
            }
            for(String i : letras_alfabeto_auxiliar){
                alfabeto_geral[indice_auxiliar_alfabeto_geral] = i;
                indice_auxiliar_alfabeto_geral++;
            }
            alfabeto_geral[indice_auxiliar_alfabeto_geral] = marca_inicio;
            indice_auxiliar_alfabeto_geral++;
            alfabeto_geral[indice_auxiliar_alfabeto_geral] = marca_branco;
            indice_auxiliar_alfabeto_geral++;
        }
        
        //leitura das transições
        //Dentro desta estrutura de repetição, sera instanciada novos objetos de Estados e salvo suas transições dentro dele.
        for(int i = 1; i < (quant_estados + 1); i++){
            boolean encontrado = false;
            //estrutura de repetição usada para saber se o estado criado é o final ou não
            //assim instanciando ele com a variavel estado_final dentro do objeto como True;
            for(int k = 0; k < estado_final.length; k++){
                if(i == estado_final[k] && encontrado == false){
                    Estados estado = new Estados(true);
                    mapEstados.put(i, estado);
                    encontrado = true;
                }else if(encontrado == false){
                    Estados estado = new Estados(false);
                    mapEstados.put(i, estado);
                    encontrado = true;
                }
            }
            for(int j = 1; j <= (quant_letras_alfabeto + quant_letras_alfabeto_auxiliar + 2); j++){
                System.out.println("----------------------------------------------------------------------");
                System.out.println("Digite o estado futuro da transição: " + i + "," + j + " (Coloque \"X\" caso queira anular a transição)");
                String leitura = scan.nextLine();
                if(leitura.equals("X")){
                    System.out.println("O campo sera anulado!");
                    System.out.println("----------------------------------------------------------------------");
                }else{
                    int estado_futuro = Integer.parseInt(leitura); 
                    System.out.println("Digite o alfabeto futuro da transição: " + i + "," + j);
                    String letra_futura = scan.nextLine();
                    System.out.println("Digite a direção da transição: " + i + "," + j + " (D para Direita ou E para Esquerda)");
                    String direcao = scan.nextLine();
                    System.out.println("----------------------------------------------------------------------");
    
                    mapEstados.get(i).setTransicao(alfabeto_geral[j-1], letra_futura, direcao, estado_futuro);
                }

            }
        }

        //Vizualição geral da tabela de transição ja montada.
        System.out.println();
        System.out.println("===== TABELA DE TRANSIÇÃO FINAL =====");
        System.out.print("   ");
        for(String i : alfabeto_geral){
            System.out.print(i + "       ");
        }
        System.out.println();
        for(int i = 1; i < quant_estados + 1; i++){
            System.out.print("S" + i + " ");
            for(int j = 1; j < (quant_letras_alfabeto + quant_letras_alfabeto_auxiliar + 1 + 2); j++){
                System.out.print(((mapEstados.get(i).getTransicao(alfabeto_geral[j-1])) == null ? "":("S" + mapEstados.get(i).getTransicao(alfabeto_geral[j-1]).getEstado_futuro()) + ","));
                System.out.print(((mapEstados.get(i).getTransicao(alfabeto_geral[j-1])) == null ? "":(mapEstados.get(i).getTransicao(alfabeto_geral[j-1]).getAlfabeto_futuro()) + ","));
                System.out.print(((mapEstados.get(i).getTransicao(alfabeto_geral[j-1])) == null ? "X       ":(mapEstados.get(i).getTransicao(alfabeto_geral[j-1]).getDirection()) + "  "));
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("----------------------------------------------------------------------");

        //é chamado o método executar() para testar e a fita principal comas informações de estados.
        executar(fita, mapEstados, estado_inicial);

        System.out.println();
        //O laço de repetição a baixo dara a oportunidade para o usuario testar outra palavra de seu gosto no programa
        //utilizando o metodo alocarFita() para mudar a fita principal e o método executar() para ver o resultado
        //da execução dessa nova palavra.
        boolean aux = true;
        while(aux){
            System.out.println("Deseja testar outra palavra? (s/n)");
            String escolha = scan.nextLine();
            if(escolha.equals("s")){
                System.out.println("Digite a nova palavra: ");
                String nova_palavra[] = scan.nextLine().split("");
                alocarFita(fita, nova_palavra, marca_inicio, marca_branco);
                System.out.println();
                executar(fita, mapEstados, estado_inicial);
                System.out.println();
            }else{
                aux = false;
            }
        }

        scan.close();
    }

    /**
     * Este método ira receber todos os alfabetos, a fita principal e a palavra dada pelo usuario
     * com estes recursos ela alocara tudo em uma sequência que dara a fita executavel final e jogara de volta para o 
     * programa principal e a executara.
     */
    public static String[] alocarFita(String fita[], String palavra[], String marca_inicio, String marca_branco){
        for(int i = 0; i < fita.length; i++){
            if(i == 0){
                fita[i] = marca_inicio;
            }else{
                fita[i] = marca_branco;
            }
        }

        //estrutura de repetição que coloca a palavra na fita principal
        for(int i = 0; i < palavra.length; i++){
            fita[i+1] = palavra[i];
        }
        
        return fita;
    }

    /**
     * Método que ira executar a fita principal usando as instruções dadas pelo usuario, caso a maquina não consiga proseguir
     * lançara um erro na tela dizendo que a palavra não foi aceita.
     */
    public static void executar(String[] fita, HashMap<Integer, Estados> mapEstados, int estado_inicial){
        String fita_final[] = new String[fita.length];
        for(int i = 0; i < fita_final.length; i++){
            fita_final[i] = fita[i];
        }
        Transicao transicao_atual = new Transicao();
        int atual_fita = 1;
        int estado_atual = estado_inicial;
        boolean aux = true;
        while(aux){
            //if para caso a proxima transição adquirida para a palavra seja nula, então a Maquina foi montada de forma errada
            //ou não aceita aquela palavra em especifico.
            if(mapEstados.get(estado_atual).getTransicao(fita_final[atual_fita]) == null){
                aux = false;
                System.out.println("Palavra não aceita");
            }else{
                transicao_atual = mapEstados.get(estado_atual).getTransicao(fita_final[atual_fita]);
                fita_final[atual_fita] = transicao_atual.getAlfabeto_futuro();
                estado_atual = transicao_atual.getEstado_futuro();
                if(transicao_atual.getDirection().equals("D")){
                    atual_fita += 1;
                }
                if(transicao_atual.getDirection().equals("E")){
                    atual_fita -= 1;
                }
                //Caso queira ver a maquina andando pela fita, tire o codigo abaixo de comentario.
                /*
                for(String i : fita_final){
                    System.out.print(i);
                }
                System.out.println();
                for(int i = 0; i <= atual_fita; i++){
                    System.out.print(i == atual_fita ? "^":" ");
                }
                System.out.println();*/
                if(mapEstados.get(estado_atual).getEstado_final() == true && atual_fita == 1){
                    aux = false;
                    System.out.println("Palavra aceita!!");
                }
            }
        }
        System.out.println("Fita final: ");
        for(String i : fita_final){
            System.out.print(i);
        }
    }
}