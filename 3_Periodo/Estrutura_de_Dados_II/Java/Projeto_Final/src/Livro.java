public class Livro {
    private String titulo;
    private int idLivro;
    private String anoPub;
    private String autor;

    public Livro(String titulo, String autor, String ano_publicacao) {
        this.setTitulo(titulo);
        this.setAutor(autor);
        this.setAnoPub(ano_publicacao);
    }

    public int getId(){
        return this.idLivro;
    }

    public void setIdLivro(int idLivro) {
        this.idLivro = idLivro;
    }

    public void setTitulo(String titulo){
        this.titulo = titulo;
    }

    public String getTitulo(){
        return this.titulo;
    }

    public String getAnoPub() {
        return anoPub;
    }

    public void setAnoPub(String anoPub) {
        this.anoPub = anoPub;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    @Override
    public String toString() {
        return "Livro [titulo=" + titulo + ", idLivro=" + idLivro + "]";
    }

    
}
