import java.sql.Connection;
import java.sql.DriverManager;

public class ConectaDB {

    private Connection conexao;

    public ConectaDB() {
        String url="jdbc:mariadb://localhost:3306/ed2";
        String usuario="root";
        String senha="root";

        try {
            conexao = DriverManager.getConnection(url, usuario, senha);
            System.out.println("conexão realizada");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            System.out.println("Drive não encontrado");
        }
    }

    public Connection getConexaoDB(){
        return conexao;
    }
}