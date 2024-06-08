import java.util.LinkedList;

public class Biblioteca {
    private LinkedList<Livro> dados;

    public Biblioteca(){
        dados = new LinkedList<Livro>();
    }

    public void inserir(Livro livro) {
        if (!dados.contains(livro)){
            dados.add(livro);
            System.out.println("Livro '" + livro.getTitulo() + "' inserido com sucesso!\n");
        } else {
            System.out.println("O livro '" + livro.getTitulo() + "' já existe na biblioteca!\n");
        }
    }

    public Livro buscaId(int idLivro) {
        for (Livro livro : dados) {
            if (livro.getId() == idLivro){
                System.out.println("Resultado da busca:");
                System.out.println(livro + "\n");
            }
        }
        return null;
    }

    public void removeLivro(int idLivro) {
        for (Livro livro : dados) {
            if (livro.getId() == idLivro) {
                dados.remove(livro);
                System.out.println("Livro '" + livro + "' removido com sucesso!\n");
            }
        }
    }

    public void listarTodos(){
        System.out.println("ID\tTitulo");
        for (Livro livro : dados) {
            String aux = livro.getId() + "\t" + livro.getTitulo();
            System.out.println(aux);
        }
        System.out.println();
    }
}
