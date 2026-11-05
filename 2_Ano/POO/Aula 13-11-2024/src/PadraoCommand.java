//Interface para o Command
interface Command {
    void execute();
}

//Classe que representa o dispositivo
class Light {
    public void on() {
        System.out.println("A luz foi ligada.");
    }

    public void off() {
        System.out.println("A luz foi desligada.");
    }
}

//Comando concreto para ligar a luz
class LightOnCommand implements Command {
    private Light light;

    public LightOnCommand(Light light) {
        this.light = light;
    }

    public void execute() {
        light.on();
    }
}

//Comando concreto para desligar a luz
class LightOffCommand implements Command {
    private Light light;

    public LightOffCommand(Light light) {
        this.light = light;
    }

    public void execute() {
        light.off();
    }
}

//Classe para o controle remoto
class RemoteControl {
    private Command command;

    public void setCommand(Command command) {
        this.command = command;
    }

    public void pressButton() {
        command.execute();
    }
}

//Classe de teste
public class PadraoCommand {
    public static void main(String[] args) {
        Light light = new Light();

        Command lightOn = new LightOnCommand(light);
        Command lightOff = new LightOffCommand(light);

        RemoteControl remote = new RemoteControl();

        //Ligar a luz
        remote.setCommand(lightOn);
        remote.pressButton();

        //Desligar a luz
        remote.setCommand(lightOff);
        remote.pressButton();
    }
}
