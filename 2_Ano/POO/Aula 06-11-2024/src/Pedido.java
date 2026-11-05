import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.List;

// O Subject
class Pedido {
    private List<Observer> observers = new ArrayList<>();
    private String status;

    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    public void setStatus(String status) {
        this.status = status;
        notifyObservers();
    }

    public String getStatus() {
        return status;
    }

    private void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(this);
        }
    }
}

// O Observer
interface Observer {
    void update(Pedido pedido);
}

class Estoque implements Observer {
    @Override
    public void update(Pedido pedido) {
        if ("Pago".equals(pedido.getStatus())) {
            JOptionPane.showMessageDialog(null, "Estoque: Pedido pago, preparar para envio.");
        }
    }
}
class Faturamento implements Observer {
    @Override
    public void update(Pedido pedido) {
        if ("Pago".equals(pedido.getStatus())) {
            JOptionPane.showMessageDialog(null, "Faturamento: Gerar nota fiscal.");
        }
    }
}