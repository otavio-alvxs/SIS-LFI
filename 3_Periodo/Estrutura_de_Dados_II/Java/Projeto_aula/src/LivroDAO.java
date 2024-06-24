import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.LinkedList;

public class LivroDAO {
    private ConectaDB conexao;

    public LivroDAO(){
        this.conexao = new ConectaDB();
    }

    // Método para inserir um livro no banco de dados
    public void inserir(Livro livro){
        ConectaDB conexao = new ConectaDB();
        String sql = "INSERT INTO livro(titulo,autor,ano) VALUES('?','?',?)"; // Problema: valores entre aspas simples
        try{
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql); // Obtém a conexão
            pst.setString(1,livro.getTitulo()); // Define o título do livro
            pst.setString(2,livro.getAutor()); // Define o autor do livro
            pst.setString(3,livro.getAnoPub());   // Define o ano do livro
            pst.execute(); // Executa a inserção

            System.out.println("Inserção ok: " + livro); // Mensagem de sucesso

        }catch (Exception e){
            System.out.println("Falha na inserção: " + e.getMessage()); // Tratamento de exceção
            
        }

    }

    // Método para consultar todos os livros no banco de dados
    public LinkedList<Livro> consultarTodos(){
        String sql = "SELECT * FROM livro"; // Consulta SQL para selecionar todos os livros
        LinkedList<Livro> lista = new LinkedList<Livro>(); // Lista para armazenar os livros consultados
        try{
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql); // Obtém a conexão e prepara a consulta
            ResultSet resultados = pst.executeQuery(); // Executa a consulta e obtém os resultados
            // Percorre os resultados obtidos
            while (resultados.next()) {
                // Recupera os dados de cada livro do resultado da consulta
                String titulo = resultados.getString("titulo");
                String autor = resultados.getString("autor");
                String ano = resultados.getString("ano");
                int id = resultados.getInt("id");
                // Cria um objeto Livro com os dados obtidos do banco de dados
                Livro obj = new Livro(titulo, ano, ano);
                obj.setAutor(autor);
                obj.setAnoPub(ano);
                obj.setIdLivro(id);
        
                lista.add(obj);
            }
            
        }catch (Exception e){
            System.out.println("Falha na consulta: " + e.getMessage()); // Tratamento de exceção
        }
        return lista; // Retorna null, deve retornar a lista de livros (lista)
        
    }
    
    // Método para consultar um livro pelo seu ID
    public Livro consultar(int id){
        Livro obj = null; // Inicializa como null para retornar null se o livro não for encontrado
        String sql = "SELECT * FROM livro WHERE id = ?";
        try{
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setInt(1,id);
            ResultSet resultados = pst.executeQuery();
            if (resultados.next()){
                String titulo = resultados.getString("titulo");
                String autor = resultados.getString("autor");
                String ano = resultados.getString("ano");
                obj = new Livro(titulo,autor, ano);
                obj.setAutor(autor);
                obj.setAutor(autor);
                obj.setAnoPub(ano);
            } else {
                System.out.println("Livro não encontrado");
            }
        } catch (SQLException e){
            System.out.println("Falha na consulta: " + e.getMessage());
        }
        return obj; // Retorna o livro encontrado ou null se não encontrar
    }

    // Método para excluir um livro pelo seu ID
    public void excluir(int id){
        String sql = "DELETE FROM livro WHERE id = ?"; // Consulta SQL para excluir um livro pelo ID
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql); // Obtém a conexão e prepara a consulta
            pst.setInt(1, id); // Define o ID do livro na consulta
            pst.executeUpdate(); // Executa a exclusão
            System.out.println("Livro excluído com sucesso"); // Mensagem de sucesso
        } catch (SQLException e) {
            System.out.println("Falha na exclusão: " + e.getMessage()); // Tratamento de exceção
        }
    }

    // Método para alterar os dados de um livro
    public void alterar(Livro livro) {
        String sql = "UPDATE livro SET titulo = ?, autor = ?, ano = ? WHERE id = ?"; // Consulta SQL para atualizar um livro
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql); // Obtém a conexão e prepara a consulta
            pst.setString(1, livro.getTitulo()); // Define o novo título do livro
            pst.setString(2, livro.getAutor());  // Define o novo autor do livro
            pst.setString(3, livro.getAnoPub());    // Define o novo ano do livro
            pst.setInt(4, livro.getId());        // Define o ID do livro na consulta

            int resultado = pst.executeUpdate(); // Executa a atualização e obtém o número de registros afetados
            if (resultado > 0) {
                System.out.println("Livro atualizado com sucesso: " + livro); // Mensagem de sucesso se o livro for atualizado
            } else {
                System.out.println("Livro não encontrado"); // Mensagem se o livro não for encontrado
            }
        } catch (SQLException e) {
            System.out.println("Falha na atualização: " + e.getMessage()); // Tratamento de exceção
        }
    }
}
