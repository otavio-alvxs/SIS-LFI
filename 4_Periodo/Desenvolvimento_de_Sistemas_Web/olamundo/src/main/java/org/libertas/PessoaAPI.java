package org.libertas;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.stream.Collector;
import java.util.stream.Collectors;

import com.google.gson.Gson;

/**
 * Servlet implementation class PessoaAPI
 */
//@WebServlet("/PessoaAPI/*")
public class PessoaAPI extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public PessoaAPI() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		PessoaDAO pdao = new PessoaDAO();
		Gson gson = new Gson();
		int id = 0;
		try {
			id = Integer.parseInt(request.getPathInfo().substring(1));
		} catch (Exception e){
		}
		String resposta;
		if (id==0) {
//			listar todos
			resposta = gson.toJson(pdao.listar());
		}else {
//			listar apenas 1
			resposta = gson.toJson(pdao.consultar(id));
		// TODO Auto-generated method stub1
		}
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);
	}
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		// pega o body da requisicao
		String body = request.getReader().lines().collect(Collectors.joining(System.lineSeparator()));
		// converte o body para um objeto java
		Gson gson = new Gson();
		Pessoa p = gson.fromJson(body, Pessoa.class);
		// salvar nova pessoa	
		PessoaDAO pdao = new PessoaDAO();
		Retorno r = new Retorno();
		// envia resposta
		r.setSucesso(pdao.inserir(p));
		r.Mensagem(r);
		String resposta = gson.toJson(r);
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);
	}
	protected void doPut(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		// pega o body da requisicao
		String body = request.getReader().lines().collect(Collectors.joining(System.lineSeparator()));
		// converte o body para um objeto java			
		Gson gson = new Gson();
		Pessoa p = gson.fromJson(body, Pessoa.class);
		int id = 0;
		try {
			id = Integer.parseInt(request.getPathInfo().substring(1));
		} catch (Exception e){
		}
		// salvar nova pessoa	
		Retorno r = new Retorno();
		PessoaDAO pdao = new PessoaDAO();
		// envia resposta
		p.setIdPessoa(id);
		r.setSucesso(pdao.alterar(p));
		r.Mensagem(r);
		String resposta = gson.toJson(r);
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);
	}
	protected void doDelete(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		int id = 0;
		try {
			id = Integer.parseInt(request.getPathInfo().substring(1));
		} catch (Exception e){
			
		}
		String body = request.getReader().lines().collect(Collectors.joining(System.lineSeparator()));
		Gson gson = new Gson();
		Retorno r = new Retorno();
		PessoaDAO pdao = new PessoaDAO();
		Pessoa p = new Pessoa();

		p.setIdPessoa(id);
		r.setSucesso(pdao.excluir(p));
		r.Mensagem(r);
		String resposta = gson.toJson(r);
		response.setHeader("content-type", "application/json");
		response.getWriter().print(resposta);
	}
}
