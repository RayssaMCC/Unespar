/*3. Crie uma classe chamada GPS contendo os seguintes atributos do tipo String:
“idioma” e “rota”. Defina dois métodos construtores: o default e outro para ligar o
GPS com o idioma português e uma rota qualquer. Elabore métodos para realizar
as seguintes funções:
- Definir idioma;
- Definir rota;
- Um método chamado “mostrar” para apresentar todos os valores atuais dos
atributos do GPS. Elabore também uma outra classe (UsaGPS) para testar
essas funcionalidades. */

package ex3;

public class GPS {
    private String idioma;
    private String rota;

    // Construtor default
    public GPS() {
        
    }

    // Construtor para ligar o GPS com idioma e rota específicos
    public GPS(String idioma, String rota) {
        this.idioma = idioma;
        this.rota = rota;
    }

    // Métodos para definir idioma e rota
    public void definirIdioma(String idioma) {
        this.idioma = idioma;
    }

    public void definirRota(String rota) {
        this.rota = rota;
    }

    // Método para mostrar os valores atuais dos atributos
    public void mostrar() {
        System.out.println("Idioma: " + idioma);
        System.out.println("Rota: " + rota);
    }
}
