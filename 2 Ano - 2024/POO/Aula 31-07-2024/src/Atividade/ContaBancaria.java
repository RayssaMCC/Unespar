package Atividade;

import java.io.*;

public class ContaBancaria {
    public String numero, titular;
    public double saldo;

    public ContaBancaria ler(String path) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(path + "/" + numero + ".txt"));
            numero = br.readLine();
            titular = br.readLine();
            saldo = Double.parseDouble(br.readLine());
            br.close();
            return this;
        } catch (IOException erro) {
            return null;
        }
    }

    public String gravar(String path) {
        try {
            File dir = new File(path);
            if (!dir.exists()) {
                dir.mkdir();
            }

            PrintWriter pw = new PrintWriter(path + "/" + numero + ".txt");
            pw.println(numero);
            pw.println(titular);
            pw.println(saldo);
            pw.flush();
            pw.close();
            return "Arquivo gravado com sucesso!";
        } catch (IOException erro) {
            return "Falha ao gravar o arquivo: " + erro.toString();
        }
    }
}