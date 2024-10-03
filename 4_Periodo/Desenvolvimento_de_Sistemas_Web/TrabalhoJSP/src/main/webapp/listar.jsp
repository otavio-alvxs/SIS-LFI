<%@page import="org.libertas.MarcaDAO"%>
<%@page import="org.libertas.Marca"%>

<%@ page import="java.util.LinkedList" %>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Lista - Marcas</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
<div class="container mt-5">
    <h2 class="text-center">Lista de Marcas</h2>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>Id da Marca</th>
                <th>Nome da Marca</th>
                <th>Descricao</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <% 
                MarcaDAO mdao = new MarcaDAO();
                LinkedList<Marca>lista = mdao.listar();
                for(Marca m : lista) {
            %>
                <tr>
                    <td><%= m.getIdMarca() %></td>
                    <td><%= m.getNomeMarca() %></td>
                    <td><%= m.getDescricao() %></td>
                    <td><%= m.getStatus() %></td>
                    <td>
						<a href='formulario.jsp?id=<%= m.getIdMarca() %>' class='btn btn-info btn-sm'>Alterar</a>
                        <a href='excluir.jsp?id=<%= m.getIdMarca() %>' class='btn btn-secondary btn-sm'>Excluir</a>
                    </td>
                    </td>
                </tr>
            <% 
                }
            %>
        </tbody>
    </table>
    <div class="text-center">
        <a href="formulario.jsp" class="btn btn-primary">Adicionar Nova Marca</a>
        <a href="index.jsp" class="btn btn-secondary">Início</a>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>

</body>
</html>