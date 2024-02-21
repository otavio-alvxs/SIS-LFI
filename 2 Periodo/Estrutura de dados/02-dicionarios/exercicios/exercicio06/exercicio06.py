import json

# Nome do arquivo JSON
arquivo_json = 'alunos.json'

# Função para carregar dados do arquivo JSON se existir
def carregar_dados():
    try:
        with open(arquivo_json, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Função para salvar dados no arquivo JSON
def salvar_dados(dados):
    with open(arquivo_json, 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

# Função para cadastrar um novo aluno
def cadastrar_aluno():
    while True:
        matricula = int(input("Digite a matrícula do aluno: "))
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        nota = float(input("Digite a nota do aluno: "))

        # Carrega os dados existentes do arquivo JSON
        alunos = carregar_dados()

        # Verifica se a matrícula já existe
        if matricula in alunos:
            print(f"Matrícula {matricula} já existe. Use outra matrícula.")
        else:
            # Cria um dicionário com as informações do aluno
            aluno_info = {"Nome": nome, "Idade": idade, "Nota": nota}
            
            # Adiciona o aluno ao dicionário principal
            alunos[matricula] = aluno_info
            print(f"Aluno cadastrado com sucesso! Matrícula: {matricula}")

            # Salva os dados atualizados no arquivo JSON
            salvar_dados(alunos)

        opcao = input("Deseja cadastrar outro aluno? (s/n): ")
        if opcao.lower() != 's':
            break

# Função para exibir todos os alunos
def exibir_alunos():
    while True:
        # Carrega os dados existentes do arquivo JSON
        alunos = carregar_dados()

        # Exibe informações de todos os alunos cadastrados
        for matricula, info in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {info['Nome']}, Idade: {info['Idade']}, Nota: {info['Nota']}")

        opcao = input("Pressione Enter para voltar ao menu principal ou digite 's' para exibir novamente: ")
        if opcao.lower() != 's':
            break

# Menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1. Cadastrar Aluno")
    print("2. Exibir Alunos")
    print("3. Sair")

    opcao_menu = input("Escolha uma opção (1/2/3): ")

    if opcao_menu == '1':
        cadastrar_aluno()
    elif opcao_menu == '2':
        exibir_alunos()
    elif opcao_menu == '3':
        print("Programa encerrado. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
