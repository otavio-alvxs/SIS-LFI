<%@page import="org.libertas.Pessoa"%>
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
	<% 
		PessoaDAO dao = new PessoaDAO();
		Pessoa p = new Pessoa();
		p.setNome(request.getParameter("nome"));
		p.setTelefone(request.getParameter("telefone"));
		p.setEmail(request.getParameter("email"));
		p.setCidade(request.getParameter("cidade"));
		p.setEndereco(request.getParameter("endereco"));
		p.setCep(request.getParameter("cep"));
		
		dao.inserir(p);
	%>
		<h1>Pessoa salva com sucesso</h1>
		<a href="index.jsp">Inicio</a>	
</body>
</html>