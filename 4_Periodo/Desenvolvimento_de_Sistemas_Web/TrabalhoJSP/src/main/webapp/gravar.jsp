<%@page import="org.libertas.MarcaDAO"%>
<%@page import="org.libertas.Marca"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Gravar - Marcas</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<% 
    Marca m = new Marca();
    MarcaDAO mdao = new MarcaDAO();

    String idMarcaParam = request.getParameter("IdMarca");
    if (idMarcaParam != null && !idMarcaParam.isEmpty()) {
        m.setIdMarca(Integer.parseInt(idMarcaParam));
    }
    
    m.setNomeMarca(request.getParameter("NomeMarca"));
    m.setDescricao(request.getParameter("Descricao"));
    m.setStatus(request.getParameter("Status"));

    mdao.salvar(m);
%>

<div class="container mt-5">
    <div class="alert alert-success text-center" role="alert">
        Marca Cadastrada com Sucesso!
    </div>
    <div class="text-center">
        <a href="index.jsp" class="btn btn-primary">Voltar ao Inicio</a>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
</body>
</html>