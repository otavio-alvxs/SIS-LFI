public class Main {
    public static void main(String[] args){
        Livro obj1 = new Livro("Engenharia de Software - Uma Abordagem Profissional", "Roger S. Pressman", "2016");
        Livro obj2 = new Livro("Estruturas de Dados e Seus Algoritmos", "MARKENZON", "2010");
        Livro obj3 = new Livro("Introdução a Sistemas de Bancos de Dados", "C.J. Date", "2004");
        Usuario obj4 = new Usuario("Otavio Alves Oliveira Costa", "otavioalvescbp@gmail.com");
        Usuario obj5 = new Usuario("Gabriel Silva", "gabriel.silva@gmail.com");

        //Instanciar biblioteca
        Biblioteca bib = new Biblioteca();
        bib.inserirLivro(obj1);
        bib.inserirLivro(obj2);
        bib.inserirLivro(obj2);
        bib.inserirLivro(obj3);
        bib.buscaId(1);
        bib.listarTodosLivros();
        bib.removeLivro(2);
        bib.listarTodosLivros();
        bib.inserirUsuario(obj4);
        bib.inserirUsuario(obj5);
        bib.listarTodosUsuarios();
        bib.consultaIDUsuario(2);
        bib.removerUsuario(2);
        bib.listarTodosUsuarios();
    }
}
