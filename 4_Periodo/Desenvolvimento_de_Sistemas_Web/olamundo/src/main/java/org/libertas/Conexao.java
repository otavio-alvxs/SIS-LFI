package org.libertas;

import java.sql.Connection;
import java.sql.DriverManager;

public class Conexao {
	private Connection connection;
	
	public Conexao() {
		try {
//			cria conexao com o banco de dados
			Class.forName("com.mysql.cj.jdbc.Driver");
			connection = DriverManager.getConnection("jdbc:mysql://54.91.193.137:3306/" + "libertas5per?verifyServerCertificate=false&useSSL=false", "libertas", "123456");
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
