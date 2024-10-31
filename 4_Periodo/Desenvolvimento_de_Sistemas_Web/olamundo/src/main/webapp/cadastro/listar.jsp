<%@page import="org.libertas.Pessoa"%>
<%@ page import="java.util.LinkedList" %>
<%@page import="org.libertas.PessoaDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<div class="container mt-5">
    <h2 class="text-center">Lista de Pessoas</h2>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>Id</th>
                <th>Nome</th>
                <th>Telefone</th>
                <th>Email</th>
                <th>Cidade</th>
                <th>Endereço</th>
                <th>CEP</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            <% 
                PessoaDAO dao = new PessoaDAO();
                LinkedList<Pessoa>lista = dao.listar();
                for(Pessoa p : lista) {
            %>
                <tr>
                    <td><%= p.getIdPessoa() %></td>
                    <td><%= p.getNome() %></td>
                    <td><%= p.getTelefone() %></td>
                    <td><%= p.getEmail() %></td>
                    <td><%= p.getCidade() %></td>
                    <td><%= p.getEndereco() %></td>
                    <td><%= p.getCep() %></td>
                    <td>
                        <a href='formulario.jsp?id=<%= p.getIdPessoa() %>' class='btn btn-warning btn-sm'>Alterar</a>
                        <a href='excluir.jsp?id=<%= p.getIdPessoa() %>' class='btn btn-danger btn-sm'>Excluir</a>
                    </td>
                </tr>
            <% 
                }
            %>
        </tbody>
    </table>
    <div class="text-center">
        <a href="formulario.jsp" class="btn btn-primary">Adicionar Nova Pessoa</a>
        <a href="index.jsp" class="btn btn-secondary">Início</a>
    </div>
</div>
</body>
</html>