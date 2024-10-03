<%@page import="org.libertas.Marca"%>
<%@page import="org.libertas.MarcaDAO"%>
<%@page import="java.util.LinkedList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Cadastrar - Marcas</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
<div class="container mt-5">
    <h2 class="text-center">Cadastro de Marcas</h2>
    <form action="gravar.jsp" method="post">
        <% 
            MarcaDAO mdao = new MarcaDAO();
            Marca marca = null;
            String IdMarcaParam = request.getParameter("id");
            if (IdMarcaParam != null && !IdMarcaParam.isEmpty()) {
                int IdMarca = Integer.parseInt(IdMarcaParam);
                marca = mdao.consultar(IdMarca); // Método para buscar a marca pelo ID
            }
            if (marca != null) {
        %>
            <input type="hidden" name="IdMarca" value="<%= marca.getIdMarca() %>">
        <% 
            } 
        %>

        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="nome" class="form-label">Nome da Marca</label>
                <input type="text" class="form-control" id="nome" name="NomeMarca" value="<%= marca != null ? marca.getNomeMarca() : "" %>" required style="width: 100%; max-width: 800px;">
            </div>
        </div>

        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="Descricao" class="form-label">Descrição</label>
                <input type="text" class="form-control" id="Descricao" name="Descricao" value="<%= marca != null ? marca.getDescricao() : "" %>" required style="width: 100%; max-width: 800px;">
            </div>
        </div>

        <div class="mb-3 d-flex justify-content-center">
            <div>
                <label for="Status" class="form-label">Status</label>
                <select class="form-control" id="Status" name="Status" required style="width: 100%; max-width: 800px;">
                    <option value="" disabled selected>Selecione o Status</option>
                    <option value="ativo" <%= (marca != null && "ativo".equals(marca.getStatus())) ? "selected" : "" %>>Ativo</option>
                    <option value="inativo" <%= (marca != null && "inativo".equals(marca.getStatus())) ? "selected" : "" %>>Inativo</option>
                </select>
            </div>
        </div>

        <div class="text-center">
            <button type="submit" class="btn btn-primary">Enviar</button>
        </div>
    </form>
</div>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
</body>
</html>