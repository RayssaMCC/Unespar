/*Faça uma classe chamada Mes que possua um método chamado getMesPorExtenso que
recebe um número inteiro, referente ao mês do ano, um código referente ao idioma (1 para
português e 2 para inglês) e retorne o mês por extenso. A tabela a seguir ilustra alguns exemplos.
Faça também outra classe para testar o método. */

package ex3;

public class Mes {
    
    public static String getMesPorExtenso(int numeroMes, int codigoIdioma) {
        // Verifica se as informações fornecidas são inválidas
        if (codigoIdioma != 1 && codigoIdioma != 2) {
            return "Código de idioma inválido";
        }
        
        if (numeroMes < 1 || numeroMes > 12) {
            return "Número do mês inválido";
        }
        
        // Se as informações são válidas, prossegue com a obtenção do mês por extenso
        if (codigoIdioma == 1) { // Português
            String[] mesesPt = {"Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"};
            return mesesPt[numeroMes - 1];
        } 
        else if (codigoIdioma == 2) { // Inglês
            String[] mesesEn = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
            return mesesEn[numeroMes - 1];
        }
        return null;
    }
}
