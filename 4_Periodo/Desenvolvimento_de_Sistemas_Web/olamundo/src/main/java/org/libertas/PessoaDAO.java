package org.libertas;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.LinkedList;

import com.mysql.cj.protocol.Resultset;

public class PessoaDAO {
//	private static LinkedList<Pessoa> lista = new LinkedList<Pessoa>();
	
	public void salvar(Pessoa p) {
		if(p.getIdPessoa()>0) {
			alterar(p);
		}else {
			inserir(p);
		}
	}
	
	
	public boolean inserir(Pessoa p) {
//		lista.add(p);
		Conexao conn = new Conexao();
		
		try {
			String sql = "INSERT INTO pessoa (nome, telefone, email, cidade, endereco, cep)" + " VALUES (?, ?, ?, ?, ?, ?)";
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setString(1, p.getNome());
			prep.setString(2, p.getTelefone());
			prep.setString(3, p.getEmail());
			prep.setString(4, p.getCidade());
			prep.setString(5, p.getEndereco());
			prep.setString(6, p.getCep());
			prep.execute();
			conn.desconecta();
			return true;
			} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			conn.desconecta();
			return false;
		}
	}
	
	public boolean alterar(Pessoa p) {
		Conexao conn = new Conexao();
		try {
			String sql1 = "SELECT * FROM pessoa WHERE idPessoa = ?";
			PreparedStatement prep1 = conn.getConnection().prepareStatement(sql1);
			prep1.setInt(1, p.getIdPessoa());
			ResultSet res = prep1.executeQuery();
			if (res.next() == false ) {
				conn.desconecta();
				return false;
			}
			
			String sql = "UPDATE pessoa SET nome = ?, telefone = ?, email = ?, cidade = ?, endereco = ?, cep = ? WHERE idPessoa = ?";
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setString(1, p.getNome());
			prep.setString(2, p.getTelefone());
			prep.setString(3, p.getEmail());
			prep.setString(4, p.getCidade());
			prep.setString(5, p.getEndereco());
			prep.setString(6, p.getCep());
			prep.setInt(7, p.getIdPessoa());
			prep.execute();
			
			return true;
			} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
		return false;
	}
	
	public boolean excluir(Pessoa p){
		Conexao conn = new Conexao();
			try {
				String sql = "SELECT * FROM pessoa WHERE idPessoa = ?";
				PreparedStatement prep = conn.getConnection().prepareStatement(sql);
				prep.setInt(1, p.getIdPessoa());
				ResultSet res = prep.executeQuery();
				if (res.next() == false ) {
					conn.desconecta();
					return false;
				}
				
				
				String sql1 = "DELETE FROM pessoa WHERE idPessoa = ?";
				PreparedStatement prep1 = conn.getConnection().prepareStatement(sql1);
				prep1.setInt(1, p.getIdPessoa());
				prep1.execute();
				conn.desconecta();
				return true;
			} catch (Exception e) {
				// TODO: handle exception
			e.printStackTrace();
			conn.desconecta();
			}
		return false;
	}
		
	public LinkedList<Pessoa> listar() {
		LinkedList<Pessoa> lista = new LinkedList<Pessoa>();
		Conexao conn = new Conexao();
		try {
			String sql = "SELECT * FROM pessoa";
			Statement sta = conn.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			while (res.next()) {
				Pessoa p = new Pessoa();
				p.setIdPessoa(res.getInt("idPessoa"));
				p.setNome(res.getString("nome"));
				p.setTelefone(res.getString("telefone"));
				p.setEmail(res.getString("email"));
				p.setCidade(res.getString("cidade"));
				p.setEndereco(res.getString("endereco"));
				p.setCep(res.getString("cep"));
				lista.add(p);
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
		return lista;
	}
	public Pessoa consultar(int id) {
		Pessoa p = new Pessoa();
		Conexao conn = new Conexao();
		try {
			String sql = "SELECT * FROM pessoa WHERE idPessoa = " + id;
			Statement sta = conn.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			p.setIdPessoa(res.getInt("idPessoa"));
			p.setNome(res.getString("nome"));
			p.setTelefone(res.getString("telefone"));
			p.setEmail(res.getString("email"));
			p.setCidade(res.getString("cidade"));
			p.setEndereco(res.getString("endereco"));
			p.setCep(res.getString("cep"));
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
		return p;
	}

}
