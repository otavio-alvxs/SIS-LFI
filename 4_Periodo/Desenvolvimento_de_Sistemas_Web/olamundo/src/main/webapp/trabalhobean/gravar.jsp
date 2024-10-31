
<%@page import="org.libertas.CidadeDAO"%>
<%@page import="org.libertas.Cidade"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
	<jsp:useBean id="c" scope="page" class="org.libertas.Cidade"/>
	<jsp:useBean id="cdao" scope="page" class="org.libertas.CidadeDAO"/>
	<jsp:setProperty property="*" name="c"/>
	
	${cdao.salvar(c)}
	<div class="container mt-5">
    <div class="alert alert-success text-center" role="alert">
        Pessoa Cadastrada com Sucesso!
    </div>
    <div class="text-center">
        <a href="index.jsp" class="btn btn-primary">Voltar ao Inicio</a>
    </div>
</div>
	
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
</body>
</html>