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
</head>
<body>
<jsp:useBean id="c" scope="page" class="org.libertas.Cidade"/>
<jsp:useBean id="cdao" scope="page" class="org.libertas.CidadeDAO"/>
<jsp:setProperty property="*" name="c"/>

${c=cdao.consultar(c.idCidade)}


<div class="container mt-5">
    <h2 class="text-center">Cadastro de Cidades</h2>
    <form action="gravar.jsp" method="post">
    <input type="hidden" name="idCidade" value="${c.idCidade}"/>
        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="nome" class="form-label">Nome da Cidade</label>
                <input type="text" class="form-control" name="nomeCidade" id="nome" value="${c.nomeCidade}" required style="width: 100%; max-width: 800px;">
            </div>
        </div>

        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="uf" class="form-label">UF</label>
                <input type="uf" class="form-control" name="uf" id="uf" value="${c.uf}"required style="width: 100%; max-width: 800px;">
            </div>
        </div>

        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="cep" class="form-label">CEP</label>
                <input type="text" class="form-control" name="cep" id="cep" value="${c.cep}"required style="width: 100%; max-width: 800px;">
            </div>
        </div>
        
		<div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="porpulacao" class="form-label">Populacao</label>
                <input type="text" class="form-control" id="populacao" name="populacao" value="${c.populacao}" required style="width: 100%; max-width: 800px;">
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