from class_bancodados import BancoDados
from class_filme import filme 
def cadastrar_filme():
    titulo = input("Digite o titulo do filme: ")
    ano_estreia = input("Digite o ano de estreia do filme: ")
    genero = input("Digite o gênero do filme: ")
    runtime = input("Digite o tempo de duração do filme: ")
    diretor = input("Digite o diretor do filme: ")
    novo_filme = filme(titulo, ano_estreia, genero, runtime, diretor)
    Banco_Dados.inserir_filme(novo_filme)
    print("Filme cadastrado com sucesso!")

def listar_filmes():
    filmes = Banco_Dados.listar_filmes()
    for filme in filmes:
        print(f"ID: {filme[0]} | Título: {filme[1]} | Ano de estreia: {filme[2]} | Gênero: {filme[3]} | Tempo de duração: {filme[4]} | Diretor: {filme[5]}")

def atualizar_filme():
    filme_id = int(input("Digite o ID do filme a ser atualizado: "))
    novo_titulo = input("Digite o novo titulo do filme: ")
    novo_ano_estreia = input("Digite o novo ano de estreia do filme: ")
    novo_genero = input("Digite o novo gênero do filme: ")
    novo_runtime = input("Digite o novo tempo de duração do filme: ")
    novo_diretor = input("Digite o novo diretor do filme: ")
    filme_atualizado = filme( novo_titulo, novo_ano_estreia, novo_genero, novo_runtime, novo_diretor)
    Banco_Dados.atualizar_filme(filme_atualizado, filme_id)
    print("Filme atualizado com sucesso!")

def deletar_filme():
    filme_id = int(input("Digite o ID do filme a ser deletado: "))
    Banco_Dados.deletar_filme(filme_id)
    print("Filme deletado com sucesso!")

Banco_Dados = BancoDados()

filme("A Origem", "2010", "Ação & Aventura", "2h 28min", "Christopher Nolan")
filme("Não! Não olhe", "2022", "Ficção Científica", "2h 10min", "Jordan Peele")
filme("WWZ: Guerra Mundial", "2013", "Terror", "1h 56min", "Marc Forster")
filme("The Revenant: O Renascido", "2015", "Drama", "2h 36min", "Alejandro González Iñárritu")
filme("Os Outros", "2001", "Terror", "1h 44min", "Alejandro Amenábar")

while True:
    print("\nMenu Principal:")
    print("1. Cadastrar filme")
    print("2. Listar filmes")
    print("3. Atualizar filme")
    print("4. Deletar filme")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_filme()
    elif opcao == '2':
        listar_filmes()
    elif opcao == '3':
        atualizar_filme()
    elif opcao == '4':
        deletar_filme()
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")

Banco_Dados.conexao.close()  # Fechar a conexão com o banco de dados