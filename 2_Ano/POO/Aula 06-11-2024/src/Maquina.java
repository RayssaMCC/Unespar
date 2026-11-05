import javax.swing.JOptionPane;

class MaquinaVendas {
    private EstadoMaquina estado;

    public MaquinaVendas() {
        // Inicialmente a máquina começa no estado de espera
        estado = new EsperandoMoeda();
    }

    public void setEstado(EstadoMaquina estado) {
        this.estado = estado;
    }

    public void inserirMoeda() {
        estado.inserirMoeda(this);
    }

    public void selecionarProduto() {
        estado.selecionarProduto(this);
    }

    public void entregarProduto() {
        estado.entregarProduto(this);
    }
}

interface EstadoMaquina {
    void inserirMoeda(MaquinaVendas maquina);
    void selecionarProduto(MaquinaVendas maquina);
    void entregarProduto(MaquinaVendas maquina);
}

class EsperandoMoeda implements EstadoMaquina {
    public void inserirMoeda(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Moeda inserida. Agora, selecione um produto.");
        maquina.setEstado(new AguardandoProduto());
    }

    public void selecionarProduto(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Você precisa inserir uma moeda primeiro.");
    }

    public void entregarProduto(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Nenhum produto foi selecionado.");
    }
}

class AguardandoProduto implements EstadoMaquina {
    public void inserirMoeda(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Você já inseriu a moeda. Agora, selecione um produto.");
    }

    public void selecionarProduto(MaquinaVendas maquina) {
        String[] produtos = {"Refrigerante", "Salgadinho", "Água"};
        String produtoSelecionado = (String) JOptionPane.showInputDialog(null, "Escolha um produto",
                "Seleção de Produto", JOptionPane.QUESTION_MESSAGE, null, produtos, produtos[0]);

        if (produtoSelecionado != null) {
            maquina.setEstado(new AguardandoEntrega(produtoSelecionado));
            maquina.entregarProduto();
        } else {
            JOptionPane.showMessageDialog(null, "Nenhum produto selecionado.");
        }
    }

    public void entregarProduto(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Nenhum produto foi selecionado.");
    }
}

class AguardandoEntrega implements EstadoMaquina {
    private String produtoSelecionado;

    public AguardandoEntrega(String produto) {
        this.produtoSelecionado = produto;
    }

    public void inserirMoeda(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Moeda já inserida. Aguardar entrega do produto.");
    }

    public void selecionarProduto(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Produto já selecionado.");
    }

    public void entregarProduto(MaquinaVendas maquina) {
        JOptionPane.showMessageDialog(null, "Produto entregue: " + produtoSelecionado);
        maquina.setEstado(new EsperandoMoeda());
    }
}