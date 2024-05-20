from classes.class_conta import Conta
from classes.class_cliente import Cliente

nome = str(input("Informe o nome: "))
cpf = int(input("Informe o CPF: "))
idade = int(input("Informe a idade: "))
rg = int(input("Informe o RG: "))

usuario1 = Cliente(nome, cpf, idade, rg)

num_conta = str(input("A respeito de sua conta, informe o número da mesma: "))
saldo = float(input("Informe seu saldo: "))
conta1 = Conta(usuario1, num_conta, saldo)
print(f"Seja bem-vindo(a) {usuario1.nome}, de conta de número {conta1.num_conta}.")

respondendo = True

while respondendo:
    opcao = int(input)("\n"'''O que deseja fazer?
                       1 - Saque
                       2 - Depósito
                       3 - Saldo
                       4 - Meus Dados
                       5 - Sair
                       Opcao: ''')
    match opcao:
        case 1:
            valor = float(input(f"Quanto deseja sacar do seu saldo de {conta1.saldo}? "))
            conta1.saque(valor)
        case 2:
            valor = float(input(f"Quanto deseja depositar? "))
            conta1.deposito(valor)
        case 3 :
            conta1.mostrar_saldo()
        case 4 :
            usuario1.mostrar_dados()
        case 5 :
            print ("Finalizando programa...")
            break
        case _:
            print("Opção inválida!!! Digite um valor entre 1 e 5.")
