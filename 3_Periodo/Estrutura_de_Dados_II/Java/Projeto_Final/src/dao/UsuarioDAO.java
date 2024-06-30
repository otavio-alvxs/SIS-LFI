package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.LinkedList;
import model.Usuario;

public class UsuarioDAO {

    private ConectaDB conexao;

    public UsuarioDAO() {
        this.conexao = new ConectaDB();
    }

    public void inserir (Usuario usuario){
        String sql = "INSERT INTO usuario(nome, email) VALUES(?, ?)";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setString(1, usuario.getNome());
            pst.setString(2, usuario.getEmail());
            pst.execute();

            System.out.println("Inserção ok: " + usuario);
        }catch (Exception e){
            System.out.println("Falha na inserção: " + e.getMessage());
        }
    }

    public void consultarTodos() {
        String sql = "SELECT * FROM usuario";
        LinkedList<Usuario> lista = new LinkedList<Usuario>();
        try{
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            ResultSet resultados = pst.executeQuery();

            while (resultados.next()) {
                int id = resultados.getInt("id");
                String nome = resultados.getString("nome");
                String email = resultados.getString("email");

                Usuario obj = new Usuario(nome, email);
                obj.setId(id);
                lista.add(obj);
            }
            for (Usuario usuario : lista) {
                System.out.println("ID: " + usuario.getId());
                System.out.println("Nome: " + usuario.getNome());
                System.out.println("Email: " + usuario.getEmail());
                System.out.println("-------------------------");
            }
        }catch (Exception e){
            System.out.println("Falha na consulta: " + e.getMessage());
        }
    }
    public Usuario consultarID(int id){
        Usuario obj = null;
        String sql = "SELECT * FROM usuario WHERE id = ?";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setInt(1, id);
            ResultSet resultados = pst.executeQuery();
            if (resultados.next()){
                String nome = resultados.getString("nome");
                String email = resultados.getString("email");
                
                obj = new Usuario(nome, email);
                obj.setId(id);
                obj.setNome(nome);
                obj.setEmail(email);
            } else {
                System.out.println("Usuario não encontrado!");
            }
        }catch (SQLException e){
            System.out.println("Falha na consulta: " + e.getMessage());
        }
        return obj;
    }

    public void excluir(int id){
        String sql = "DELETE FROM usuario WHERE id = ?";
        try{
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setInt(1, id);
            pst.executeUpdate();
            System.out.println("Usuario excluido com sucesso");
        } catch (SQLException e) {
            System.out.println("Falha na exclulsão: " + e.getMessage());
        }
    }

    public void alterar(Usuario usuario){
        String sql = "UPDATE usuario SET nome = ?, email = ? WHERE id = ?";
        try {
            PreparedStatement pst = conexao.getConexaoDB().prepareStatement(sql);
            pst.setString(1, usuario.getNome());
            pst.setString(2, usuario.getEmail());
            pst.setInt(3, usuario.getId());

            int resultado = pst.executeUpdate();
            if (resultado > 0){
                System.out.println("Usuario atualizado com sucesso: " + usuario);
            }
            else {
                System.out.println("Usuario não encontrado");
            }
        } catch (SQLException e) {
            System.out.println("Falha na atualização: " + e.getMessage());
        }
    }
}