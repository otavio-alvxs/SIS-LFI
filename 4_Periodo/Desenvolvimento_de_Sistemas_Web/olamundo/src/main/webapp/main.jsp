<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1 align="center">Matato</h1>
	<%@ include file="menu.jsp" %>
	<%
		int a = 1;
		int b = 2;
		int c = a+b;
	%>
	<%!
		public double media(double a, double b){
			return(a+b)/2;
	}
	%>
	<div style="font-size:40px">
		<%= c %>
		<br>
		<%=media(a,b) %>
	</div>
</body>
</html>