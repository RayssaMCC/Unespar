package pessoas;

public class Principal {

    public static void main(String[] args) {

        AlunoMestrado aluno = new AlunoMestrado();

        aluno.setCodigo(1);
        aluno.setNome("Zeca");
        aluno.setTelefone("(43) 99999-9999");
        aluno.endereco = "Paraná";

        aluno.setNumMatricula(2026001);
        aluno.setMedia(8.5);
        aluno.setFaltas(3);

        aluno.setConceitoDissertacao(9.0);
        aluno.setNotaDissertacao(8.5);

        aluno.imprimeDados();

        if (aluno.aprovado()) {
            System.out.println("Aluno aprovado.");
        } else {
            System.out.println("Aluno não aprovado.");
        }
    }
}
