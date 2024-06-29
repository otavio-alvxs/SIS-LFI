import java.util.Scanner;
public class Main {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int opcao;

        do {
            System.out.println("\n\nMenu:");
            System.out.println("1. Gerenciar Tabela Usuário");
            System.out.println("2. Gerenciar Tabela Livro");
            System.out.println("0. Sair");
            System.out.print("Digite sua opção: ");

            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    gerenciarUsuarios();
                    break;
                case 2:
                    gerenciarLivros();
                    break;
                case 0:
                    System.out.println("Saindo do programa...");
                    break;
                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        } while (opcao != 0);

        scanner.close();
    }

    private static void gerenciarLivros() {
        LivroDAO livroDAO = new LivroDAO();
        int opcaoLivro;
        int idLivro;
        String titulo, autor, anoPub;
    
        do {
            System.out.println("\n\nGerenciar Livros:");
            System.out.println("");
            System.out.println("1. Inserir Livro");
            System.out.println("2. Alterar Livro");
            System.out.println("3. Remover Livro");
            System.out.println("4. Consultar Livro por ID");
            System.out.println("5. Listar Todos os Livros");
            System.out.println("0. Voltar ao Menu Principal");
            System.out.print("Digite sua opção: ");
    
            opcaoLivro = scanner.nextInt();
    
            if (opcaoLivro < 0 || opcaoLivro > 5) {
                System.out.println("Opção inválida! Digite novamente: ");
                opcaoLivro = scanner.nextInt();
            }
    
            switch (opcaoLivro) {
                case 1:
                    System.out.print("Digite o título do livro: ");
                    titulo = scanner.next();
                    System.out.print("Digite o autor do livro: ");
                    autor = scanner.next();
                    System.out.print("Digite o ano de publicação do livro: ");
                    anoPub = scanner.next();
    
                    Livro novoLivro = new Livro(titulo, autor, anoPub);
                    livroDAO.inserir(novoLivro);
                    System.out.println("Livro " + titulo + " inserido com sucesso!");
                    break;
    
                case 2:
                    System.out.print("Digite o ID do livro a ser alterado: ");
                    idLivro = scanner.nextInt();
    
                    Livro livroAntigo = livroDAO.consultar(idLivro);
    
                    if (livroAntigo != null) {
                        System.out.print("Digite o novo título do livro: ");
                        titulo = scanner.next();
                        System.out.print("Digite o novo autor do livro: ");
                        autor = scanner.next();
                        System.out.print("Digite o novo ano de publicação do livro: ");
                        anoPub = scanner.next();
    
                        livroAntigo.setTitulo(titulo);
                        livroAntigo.setAutor(autor);
                        livroAntigo.setAnoPub(anoPub);
    
                        livroDAO.alterar(livroAntigo);
                        System.out.println("Livro " + titulo + " atualizado com sucesso!");
                    } else {
                        System.out.println("Livro não encontrado!");
                    }
                    break;
    
                case 3:
                    System.out.print("Digite o ID do livro a ser removido: ");
                    idLivro = scanner.nextInt();
    
                    Livro livroRemovido = livroDAO.consultar(idLivro);
    
                    if (livroRemovido != null) {
                        livroDAO.excluir(idLivro);
                        System.out.println("Livro " + livroRemovido.getTitulo() + " removido com sucesso!");
                    } else {
                        System.out.println("Livro não encontrado!");
                    }
                    break;
    
                case 4:
                    System.out.print("Digite o ID do livro que deseja consultar: ");
                    idLivro = scanner.nextInt();
    
                    Livro livroConsultado = livroDAO.consultar(idLivro);
    
                    if (livroConsultado != null) {
                        System.out.println("Livro encontrado:");
                        System.out.println(livroConsultado);
                    } else {
                        System.out.println("Livro não encontrado!");
                    }
                    break;
    
                case 5:
                    System.out.println("\nListando todos os livros: ");
                    livroDAO.consultarTodos();
                    break;
    
                case 0:
                    System.out.println("Voltando ao Menu Principal...");
                    break;
    
                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        } while (opcaoLivro != 0);
    }

    private static void gerenciarUsuarios(){
        UsuarioDAO usuarioDAO = new UsuarioDAO();
        int opcao;
        int id;
        String usuario, email, nome;

        do {
            System.out.println("\nGerenciar Usuários:");
            System.out.println("");
            System.out.println("1. Inserir Usuário");
            System.out.println("2. Alterar Usuário");
            System.out.println("3. Remover Usuário");
            System.out.println("4. Consultar Usuário por ID");
            System.out.println("5. Listar Todos os Usuários");
            System.out.println("0. Voltar ao Menu");
            System.out.println();
            System.out.print("Digite sua opção: ");

            opcao = scanner.nextInt();

            if (opcao < 0 || opcao > 5) {
                System.out.println("Opção inválida! Digite novamente: ");
                opcao = scanner.nextInt();
            }
            
            switch (opcao) {
                case 1:
                    System.out.print("Digite o nome do usuário: ");
                    usuario = scanner.next();
                    System.out.print("Digite o email do usuário: ");
                    email = scanner.next();
                    Usuario novoUsuario = new Usuario(usuario, email);
                    usuarioDAO.inserir(novoUsuario);
                    System.out.print("Usuário " + usuario + " inserido com sucesso!");
                    break;

                case 2:
                    System.out.println("Digite o id do usuário a ser alterado: ");
                    id = scanner.nextInt();
                    Usuario usuarioAntigo = usuarioDAO.consultarID(id);
                    if (usuarioAntigo != null){
                        System.out.println("Alterando o usuário: " + usuarioAntigo);
                        System.out.println("Digite o novo nome do usuário: ");
                        nome = scanner.next();
                        System.out.println("Digite o novo email do usuário: ");
                        email = scanner.next();

                        usuarioAntigo.setNome(nome);
                        usuarioAntigo.setEmail(email);

                        usuarioDAO.alterar(usuarioAntigo);
                        System.out.println("Usuário " + nome + " atualizado com sucesso!");
                    }
                    break;

                case 3:
                    System.out.print("Digite o ID do usuário a ser removido: ");
                    id = scanner.nextInt();
                    Usuario tmp = usuarioDAO.consultarID(id);
                    if (tmp != null){
                        usuarioDAO.excluir(id);
                        System.out.print("Usuário " + tmp + " excluído com sucesso!");
                    } break;

                case 4:
                System.out.print("Digite o ID que deseja consultar: ");
                id = scanner.nextInt();
                Usuario response = usuarioDAO.consultarID(id);
                System.out.println("Usuário retornado: " + response);
                break;

                case 5:
                    System.out.println("Listando todos os usuários: ");
                    usuarioDAO.consultarTodos();
                    break;

                case 0:
                    System.out.println("Voltando ao Menu...");
                    break;

                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        } while (opcao != 0);
    }
}
