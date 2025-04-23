<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado da Calculadora</title>
</head>
<body>
    <h1>Resultado</h1>
    <%
        try {
            // Obtém os parâmetros enviados pelo formulário
            double numero1 = Double.parseDouble(request.getParameter("numero1"));
            double numero2 = Double.parseDouble(request.getParameter("numero2"));
            String operacao = request.getParameter("operacao");
            double resultado = 0;

            // Realiza o cálculo baseado na operação escolhida
            switch (operacao) {
                case "+":
                    resultado = numero1 + numero2;
                    break;
                case "-":
                    resultado = numero1 - numero2;
                    break;
                case "*":
                    resultado = numero1 * numero2;
                    break;
                case "/":
                    if (numero2 != 0) {
                        resultado = numero1 / numero2;
                    } else {
                        out.println("<p>Erro: Divisão por zero não é permitida.</p>");
                        return;
                    }
                    break;
                default:
                    out.println("<p>Operação inválida.</p>");
                    return;
            }

            // Exibe o resultado
            out.println("<p>Resultado: " + resultado + "</p>");
        } catch (NumberFormatException e) {
            out.println("<p>Erro: Certifique-se de que os valores inseridos são números.</p>");
        }
    %>
    <a href="calculadora.html">Voltar</a>
</body>
</html>
