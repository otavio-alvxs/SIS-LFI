package org.libertas;

import java.sql.Connection;
import java.sql.DriverManager;

public class ConexaoTrabalho {
	private Connection connection;
	
	public ConexaoTrabalho() {
		try {
//			cria conexao com o banco de dados
			Class.forName("org.mariadb.jdbc.Driver");
			connection = DriverManager.getConnection("jdbc:mariadb://127.0.0.1:3306/cidade", "root", "root" );
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
	public void desconecta() {
		try {
			
			
			connection.close();
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}

	public Connection getConnection() {
		return connection;
	} 

	public void setConnection(Connection connection) {
		this.connection = connection;
	}
	
}
