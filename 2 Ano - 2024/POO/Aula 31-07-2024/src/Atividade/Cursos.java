package Atividade;

import java.io.*;

public class Cursos {
    public String codigo, nome, descricao;
    public int duracao; // duração em horas

    public Cursos ler(String path) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(path + "/" + codigo + ".txt"));
            codigo = br.readLine();
            nome = br.readLine();
            descricao = br.readLine();
            duracao = Integer.parseInt(br.readLine());
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

            PrintWriter pw = new PrintWriter(path + "/" + codigo + ".txt");
            pw.println(codigo);
            pw.println(nome);
            pw.println(descricao);
            pw.println(duracao);
            pw.flush();
            pw.close();
            return "Arquivo gravado com sucesso!";
        } catch (IOException erro) {
            return "Falha ao gravar o arquivo: " + erro.toString();
        }
    }
}