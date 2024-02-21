#2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input('Nome de usuário: '))
senha = str(input('Senha: '))

while usuario == senha:
    print('A senha não pode ser igual ao nome de usuário, por favor tente novamente.')
    usuario = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))

print ('Tudo certo!')
print ('Fim da execução')
