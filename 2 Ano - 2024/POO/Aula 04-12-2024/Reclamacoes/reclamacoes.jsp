<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reclamação Recebida</title>
</head>
<body>
    <h1>Portal do Cidadão - Reclamação Recebida</h1>
    <%
        // Obtém os dados do formulário
        String endereco = request.getParameter("endereco");
        String tipoProblema = request.getParameter("tipo");
        String descricao = request.getParameter("descricao");

        // Exibe a confirmação e as informações fornecidas
        out.println("<p>Obrigado por sua reclamação!</p>");
        out.println("<p><strong>Endereço informado:</strong> " + endereco + "</p>");
        out.println("<p><strong>Tipo de problema:</strong> " + tipoProblema + "</p>");
        out.println("<p><strong>Descrição do problema:</strong></p>");
        out.println("<p>" + descricao + "</p>");
    %>
    <a href="reclamacoes.html">Voltar</a>
</body>
</html>
