<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Projeto com Bootstrap</title>
    <link rel="stylesheet" href="<%= request.getContextPath() %>/css/bootstrap.min.css"> <!-- Se usar arquivos locais -->
    <!-- Ou use CDN -->
    <!-- <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css"> -->
</head>
<body>
    <div class="container">
        <h1 class="text-center">Bem-vindo ao Meu Projeto!</h1>
        <p class="lead">Esta é uma página de exemplo utilizando Bootstrap.</p>
        <button class="btn btn-primary">Clique Aqui</button>
    </div>

    <script src="<%= request.getContextPath() %>/js/bootstrap.bundle.min.js"></script> <!-- Se usar arquivos locais -->
    <!-- Ou use CDN -->
    <!-- <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> -->
    <!-- <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script> -->
</body>
</html>