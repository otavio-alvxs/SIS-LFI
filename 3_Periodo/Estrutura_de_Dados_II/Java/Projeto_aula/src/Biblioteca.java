import java.util.LinkedList;

public class Biblioteca {
    private LinkedList<Livro> dadosLivro;
    private LinkedList<Usuario> dadosUsuario;

    public Biblioteca(){
        dadosLivro = new LinkedList<Livro>();
        dadosUsuario = new LinkedList<Usuario>();
    }

    public void inserirLivro(Livro livro) {
        System.out.println("Inserindo Livro...");
        if (!dadosLivro.contains(livro)){
            dadosLivro.add(livro);
            System.out.println("Livro '" + livro.getTitulo() + "' inserido com sucesso!\n");
        } else {
            System.out.println("O livro '" + livro.getTitulo() + "' já existe na biblioteca!\n");
        }
    }

    public Livro buscaId(int idLivro) {
        System.out.println("Buscando Livro...");
        for (Livro livro : dadosLivro) {
            if (livro.getId() == idLivro){
                System.out.println("Resultado da busca:");
                System.out.println(livro + "\n");
            }
        }
        return null;
    }

    public void removeLivro(int idLivro) {
        System.out.println("Removendo Livro...");
        for (Livro livro : dadosLivro) {
            if (livro.getId() == idLivro) {
                dadosLivro.remove(livro);
                System.out.println("Livro '" + livro + "' removido com sucesso!\n");
            }
        }
    }

    public void listarTodosLivros() {
        System.out.println("Listando Livros...");
        System.out.println("ID\tTitulo");
        dadosLivro.sort((livro1, livro2) -> Integer.compare(livro1.getId(), livro2.getId()));
        for (Livro livro : dadosLivro) {
            String aux = livro.getId() + "\t" + livro.getTitulo();
            System.out.println(aux);
        }
        System.out.println();
    }

    public void inserirUsuario(Usuario usuario){
        System.out.println("Inserindo Usuário...");
        if (dadosUsuario.contains(usuario)) {
            System.out.println("O usuário " + usuario.getNome() + " já está cadastrado na biblioteca.");
        } else {
            dadosUsuario.add(usuario);
            System.out.println("O usuário " + usuario.getNome() + " foi cadastrado com sucesso.");
        }
        System.out.println();
    }

    public Usuario consultaIDUsuario(int id) {
        System.out.println("Consultando Usuário...");
        for (Usuario usuario : dadosUsuario) {
            if (usuario.getId() == id) {
                return usuario;
            }
        }
        System.out.println("Usuário não cadastrado");
        System.out.println();
        return null;
    }

    public void removerUsuario(int id){
        System.out.println("Removendo Usuário...");
        for (Usuario usuario : dadosUsuario) {
            if (usuario.getId() == id) {
                dadosUsuario.remove(usuario);
                System.out.println("O cadastro do usuário " + usuario.getNome() + " foi removido.");
            }
        }
        System.out.println();
    }

    public void listarTodosUsuarios(){
        System.out.println("Listando Usuários...");
        System.out.println("ID\tNome\tE-mail");
        for (Usuario usuario : dadosUsuario) {
            String aux = usuario.getId() + "\t" + usuario.getNome() + "\t" + usuario.getEmail();
            System.out.println(aux);
        }
        System.out.println();
    }
}
