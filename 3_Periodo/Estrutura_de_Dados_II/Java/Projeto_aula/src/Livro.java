public class Livro {
    private String titulo;
    private int idLivro;
    private String anoPub;
    private String autor;
    private static int contador = 0;

    public Livro (String titulo){
        this.setTitulo(titulo);
        // System.out.println(contador);
        contador += 1;
        this.setIdLivro(contador);
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