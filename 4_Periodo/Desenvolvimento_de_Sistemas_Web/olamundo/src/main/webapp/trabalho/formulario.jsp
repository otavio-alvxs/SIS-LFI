<%@page import="org.libertas.Pessoa"%>
<%@page import="org.libertas.PessoaDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Cadastrar Cidades</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<style>
	
</style>
</head>
<body>
<div class="container mt-5">
    <h2 class="text-center">Cadastro de Cidades</h2>
    <form action="gravar.jsp" method="post">
        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="nome" class="form-label">Nome da Cidade</label>
                <input type="text" class="form-control" id="nome" name="nomeCidade" required style="width: 100%; max-width: 800px;">
            </div>
        </div>

        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="uf" class="form-label">UF</label>
                <input type="uf" class="form-control" id="uf" name="uf" required style="width: 100%; max-width: 800px;">
            </div>
        </div>

        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="cep" class="form-label">CEP</label>
                <input type="text" class="form-control" id="cep" name="cep" required style="width: 100%; max-width: 800px;">
            </div>
        </div>
        
		<div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="porpulacao" class="form-label">Populacao</label>
                <input type="text" class="form-control" id="populacao" name="populacao" required style="width: 100%; max-width: 800px;">
            </div>
        </div>
		
        <div class="text-center">
            <button type="submit" class="btn btn-primary">Enviar</button>
        </div>
    </form>
</div>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
</body>
</html>