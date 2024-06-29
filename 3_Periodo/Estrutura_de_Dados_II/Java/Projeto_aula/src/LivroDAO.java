import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.LinkedList;

public class LivroDAO {

    private ConectaDB conexao;

    public LivroDAO() {
        this.conexao = new ConectaDB();
    }

    public void inserir(Livro livro) {
        String sql = "INSERT INTO livro(titulo,anoPub,autor) VALUES(?,?,?)";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setString(1, livro.getTitulo());
            pst.setString(2, livro.getAnoPub());
            pst.setString(3, livro.getAutor());
            pst.execute();

            System.out.println("Inserção ok: " + livro);

        } catch (Exception e) {
            System.out.println("Falha na inserção: " + e.getMessage());
        } new ConectaDB().desconectaDB();
    }

    public void consultarTodos() {
        String sql = "SELECT * FROM livro";
        LinkedList<Livro> lista = new LinkedList<>();
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            ResultSet resultados = pst.executeQuery();

            while (resultados.next()) {
                String titulo = resultados.getString("titulo");
                String autor = resultados.getString("autor");
                String anoPub = resultados.getString("anoPub");
                int id = resultados.getInt("id");

                Livro obj = new Livro(titulo, autor, anoPub);
                obj.setIdLivro(id);
                lista.add(obj);
            }

            for (Livro livro : lista) {
                System.out.println("\nID: " + livro.getId());
                System.out.println("Título: " + livro.getTitulo());
                System.out.println("Ano de Publicação: " + livro.getAnoPub());
                System.out.println("Autor: " + livro.getAutor());
            }

        } catch (Exception e) {
            System.out.println("Falha na consulta: " + e.getMessage());
        }
    }

    public Livro consultar(int id) {
        Livro obj = null;
        String sql = "SELECT * FROM livro WHERE id = ?";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setInt(1, id);
            ResultSet resultados = pst.executeQuery();

            if (resultados.next()) {
                String titulo = resultados.getString("titulo");
                String anoPub = resultados.getString("anoPub");
                String autor = resultados.getString("autor");
                obj = new Livro(titulo, anoPub, autor);
                obj.setIdLivro(id);
            } else {
                System.out.println("Livro não encontrado");
            }

        } catch (SQLException e) {
            System.out.println("Falha na consulta: " + e.getMessage());
        }

        return obj;
    }

    public void excluir(int id) {
        String sql = "DELETE FROM livro WHERE id = ?";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setInt(1, id);
            pst.executeUpdate();
            System.out.println("Livro excluído com sucesso");

        } catch (SQLException e) {
            System.out.println("Falha na exclusão: " + e.getMessage());
        }
    }

    public void alterar(Livro livro) {
        String sql = "UPDATE livro SET titulo = ?, anoPub = ?, autor = ? WHERE id = ?";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setString(1, livro.getTitulo());
            pst.setString(2, livro.getAnoPub());
            pst.setString(3, livro.getAutor());
            pst.setInt(4, livro.getId());

            int resultado = pst.executeUpdate();
            if (resultado > 0) {
                System.out.println("Livro atualizado com sucesso: " + livro);
            } else {
                System.out.println("Livro não encontrado");
            }

        } catch (SQLException e) {
            System.out.println("Falha na atualização: " + e.getMessage());
        }
    }
}
