package Atividades;

import javax.swing.*;
import java.awt.*;
import java.time.DayOfWeek;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class HorarioAtendimento {

    public static void main(String[] args) {
        //Cria o frame
        JFrame frame = new JFrame("Verificação de Horário");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);

        //Cria o painel
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        frame.add(panel);

        //Cria o label para exibir a mensagem
        JLabel messageLabel = new JLabel("", SwingConstants.CENTER);
        panel.add(messageLabel, BorderLayout.CENTER);

        //Verifica o horário e atualiza a mensagem
        String mensagem = verificarHorario();
        messageLabel.setText(mensagem);

        //Exibe o frame
        frame.setVisible(true);
    }

    //Método para verificar o horário e retornar a mensagem correspondente
    public static String verificarHorario() {
        LocalDateTime agora = LocalDateTime.now();
        DayOfWeek diaDaSemana = agora.getDayOfWeek();
        int hora = agora.getHour();
        String situacao;

        //Verifica se é dia útil e horário de expediente
        if (diaDaSemana != DayOfWeek.SATURDAY && diaDaSemana != DayOfWeek.SUNDAY) {
            if (hora >= 8 && hora < 17) {
                situacao = "Estamos atendendo";
            } else {
                situacao = "Expediente encerrado";
            }
        } else {
            situacao = "Expediente encerrado";
        }

        //Formata a data e hora para PT-BR
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("EEEE - HH:mm", Locale.forLanguageTag("pt-BR"));
        String dataHoraFormatada = agora.format(formatter);

        return dataHoraFormatada + " - " + situacao;
    }
}