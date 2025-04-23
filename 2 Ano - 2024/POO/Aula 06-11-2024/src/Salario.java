import java.util.Stack;

// Memento que armazena o estado do salário
class SalarioMemento {
    private final double estadoSalario;

    public SalarioMemento(double estadoSalario) {
        this.estadoSalario = estadoSalario;
    }

    public double getEstadoSalario() {
        return estadoSalario;
    }
}

// Classe Originator que realiza os cálculos de salário
class SalarioCalculador {
    private double salario;

    public SalarioCalculador(double salarioInicial) {
        this.salario = salarioInicial;
    }

    public void adicionarBonus(double valor) {
        salario += valor;
    }

    public void aplicarDesconto(double valor) {
        salario -= valor;
    }

    public SalarioMemento salvarEstado() {
        return new SalarioMemento(salario);
    }

    public void restaurarEstado(SalarioMemento memento) {
        this.salario = memento.getEstadoSalario();
    }

    public double getSalario() {
        return salario;
    }
}

// CareTaker que mantém uma pilha de Mementos
class CareTaker {
    private Stack<SalarioMemento> historico = new Stack<>();

    public void salvarMemento(SalarioMemento memento) {
        historico.push(memento);
    }

    public SalarioMemento desfazer() {
        if (!historico.isEmpty()) {
            return historico.pop();
        }
        return null;
    }
}