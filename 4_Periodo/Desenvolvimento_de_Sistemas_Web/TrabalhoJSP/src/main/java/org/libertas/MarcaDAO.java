package org.libertas;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.LinkedList;

public class MarcaDAO {

	public void salvar(Marca m) {
		if(m.getIdMarca() > 0) {
			alterar(m);
		}else {
			inserir(m);
		}
	}
	
	public void inserir(Marca m) {
//		lista.add(p);
		Conexao conn = new Conexao();
		
		try {
			String sql = "INSERT INTO Marcas (NomeMarca, Descricao, Status)" + " VALUES (?, ?, ?)";
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setString(1, m.getNomeMarca());
			prep.setString(2, m.getDescricao());
			prep.setString(3, m.getStatus());
			prep.execute();
;		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
	}
	
	public void alterar(Marca m) {
		Conexao conn = new Conexao();
		try {
			String sql = "UPDATE Marcas SET" + " NomeMarca = ?," + " Descricao = ?," + " Status = ?" + " WHERE IdMarca = ?";
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setString(1, m.getNomeMarca());
			prep.setString(2, m.getDescricao());
			prep.setString(3, m.getStatus());
			prep.setInt(4, m.getIdMarca());
			prep.execute();
			} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
	}
	
	public void excluir(Marca m) {
		Conexao conn = new Conexao();
		try {
			String sql = "DELETE FROM Marcas WHERE IdMarca = ?";
			PreparedStatement prep = conn.getConnection().prepareStatement(sql);
			prep.setInt(1, m.getIdMarca());
			prep.execute();
			} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
	}

	public LinkedList<Marca> listar() {
		LinkedList<Marca> lista = new LinkedList<Marca>();
		Conexao conn = new Conexao();
		try {
			String sql = "SELECT * FROM Marcas";
			Statement sta = conn.getConnection().createStatement();
			ResultSet res = sta.executeQuery(sql);
			while (res.next()) {
				Marca m = new Marca();
				m.setIdMarca(res.getInt("IdMarca"));
				m.setNomeMarca(res.getString("NomeMarca"));
				m.setDescricao(res.getString("Descricao"));
				m.setStatus(res.getString("Status"));
				lista.add(m);
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		conn.desconecta();
		return lista;
	}
	
	public Marca consultar(int id) {
	    Marca m = new Marca();
	    Conexao conn = new Conexao();
	    try {
	        String sql = "SELECT * FROM Marcas WHERE IdMarca = ?";
	        PreparedStatement prep = conn.getConnection().prepareStatement(sql);
	        prep.setInt(1, id);
	        ResultSet res = prep.executeQuery();
	        if (res.next()) {
	            m.setIdMarca(res.getInt("IdMarca"));
	            m.setNomeMarca(res.getString("NomeMarca"));
	            m.setDescricao(res.getString("Descricao"));
	            m.setStatus(res.getString("Status"));
	        }
	    } catch (Exception e) {
	        e.printStackTrace();
	    }
	    conn.desconecta();
	    return m;
	}

}
