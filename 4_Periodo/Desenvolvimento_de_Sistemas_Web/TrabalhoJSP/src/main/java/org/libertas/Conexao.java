package org.libertas;

import java.sql.Connection;
import java.sql.DriverManager;

public class Conexao {
    private Connection connection;

    public Conexao() {
        try {
            Class.forName("org.mariadb.jdbc.Driver");
            connection = DriverManager.getConnection("jdbc:mariadb://localhost:3306/Trabalho", "root", "root");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void desconecta() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
            }
        } catch (Exception e) {
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