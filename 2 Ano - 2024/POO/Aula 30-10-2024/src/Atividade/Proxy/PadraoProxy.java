package Atividade.Proxy;

public class PadraoProxy {
    public static void main(String[] args) {
        System.out.println(
        new Cliente().cumprimentar("Renato"));
    }
    
}

interface InterfaceSujeito {
    String cumprimentar(String nome);
}

class SujeitoReal implements InterfaceSujeito {

    @Override
    public String cumprimentar(String nome) {
        return "Olá " + nome;
    }
}

class SujeitoRealProxy implements InterfaceSujeito {
    private SujeitoReal sujeitoReal = new SujeitoReal();

    @Override
    public String cumprimentar(String nome) {
        System.out.println("Proxy: registrando antes de cumprimentar");
        String resultado = sujeitoReal.cumprimentar(nome);
        System.out.println("Proxy: registrando depois de cumprimentar");
        return resultado;
    }
}

class Cliente {
    public String cumprimentar(String nome) {
        var sujeitoRealProxy = new SujeitoRealProxy();

        return sujeitoRealProxy.cumprimentar(nome);
    }
}
