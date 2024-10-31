package org.libertas;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.LinkedList;

public class CidadeDAO {

	public void salvar(Cidade c) {
		if(c.getIdCidade()>0) {
			alterar(c);
		}else {
			inserir(c);
		}
	}
	
	public void inserir(Cidade c) {
//		lista.add(p);
		Conexao conn = new Conexao();
		
		try {
			String sql = "INSERT INTO cidades (nomeCidade, uf, cep, populacao)" + " VALUES (?, ?, ?, ?)";
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setString(1, c.getNomeCidade());
			prep.setString(2, c.getUf());
			prep.setString(3, c.getCep());
			prep.setString(4, c.getPopulacao());
			prep.execute();
;		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
	}
	
	public void alterar(Cidade c) {
		Conexao conn = new Conexao();
		try {
			String sql = "UPDATE cidades SET " + "nomeCidade = ?, uf = ?, " + " cep = ?, populacao = ? WHERE idCidade = " + c.getIdCidade();
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setString(1, c.getNomeCidade());
			prep.setString(2, c.getUf());
			prep.setString(3, c.getCep());
			prep.setString(4, c.getPopulacao());
			prep.execute();
			} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
	}
	
	public void excluir(Cidade c) {
		Conexao conn = new Conexao();
		try {
			String sql = "DELETE FROM cidades WHERE idCidade = ?";
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setInt(1, c.getIdCidade());
			prep.execute();
			} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
	}

	public LinkedList<Cidade> listar() {
		LinkedList<Cidade> lista = new LinkedList<Cidade>();
		Conexao conn = new Conexao();
		try {
			String sql = "SELECT * FROM cidades";
			Statement sta = conn.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			while (res.next()) {
				Cidade c = new Cidade();
				c.setIdCidade(res.getInt("idCidade"));
				c.setNomeCidade(res.getString("nomeCidade"));
				c.setUf(res.getString("uf"));
				c.setCep(res.getString("cep"));
				c.setPopulacao(res.getString("populacao"));
				lista.add(c);
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
		return lista;
	}
	public Cidade consultar(int id) {
		Cidade c = new Cidade();
		Conexao conn = new Conexao();
		try {
			String sql = "SELECT * FROM cidades WHERE idCidade = " + id;
			Statement sta = conn.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			if (res.next()) {
				c.setIdCidade(res.getInt("idCidade"));
				c.setNomeCidade(res.getString("nomeCidade"));		
				c.setUf(res.getString("uf"));
				c.setCep(res.getString("cep"));
				c.setPopulacao(res.getString("populacao"));
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			
		}
		conn.desconecta();
		return c;
	}

}

