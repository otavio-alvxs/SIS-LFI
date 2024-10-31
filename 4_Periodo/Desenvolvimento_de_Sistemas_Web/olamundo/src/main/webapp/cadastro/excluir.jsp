<%@page import="org.libertas.PessoaDAO"%>
<%@page import="org.libertas.Pessoa"%>
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
		Pessoa p = new Pessoa();
		p.setIdPessoa(Integer.parseInt(request.getParameter("id")));;
		PessoaDAO pdao = new PessoaDAO();
		pdao.excluir(p);
	%>
	
		Registro excluído com sucesso</br>
		<a href="index.jsp">Voltar pro inicio</a>
</body>
</html>