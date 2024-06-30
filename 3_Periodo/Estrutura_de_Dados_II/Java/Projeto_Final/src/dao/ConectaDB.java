package dao;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConectaDB {

    private Connection conexao;

    public ConectaDB() {
        String url="jdbc:mariadb://localhost:3306/ed2";
        String usuario="root";
        String senha="root";

        try {
            System.out.println("Iniciando conexão com o banco de dados...");
            conexao = DriverManager.getConnection(url, usuario, senha);
            System.out.println("Conexão realizada!\n");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            System.out.println("Drive não encontrado");
        }
    }

    public Connection getConexaoDB(){
        return conexao;
    }

    public void desconectaDB() {
        if (conexao != null) {
            try {
                conexao.close();
                System.out.println("Conexão fechada");
            } catch (SQLException e) {
                System.out.println("Erro ao fechar conexão: " + e.getMessage());
            }
        }
    }
}