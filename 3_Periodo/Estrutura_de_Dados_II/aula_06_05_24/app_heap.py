from Tarefa import Task
import heapq

lista_tarefas = []

def menu():
    print ("-" * 10)
    print ("1 - Adicionar Tarefa")
    print ("2 - Realizar(Remover) Tarefa")
    print ("3 - Consultar Tarefas")
    print ("4 - Sair")

def adicionar():
    titulo = str(input("Digite o titulo: "))
    descricao = str(input("Digite a descricao: "))
    obj = Task(titulo)
    obj.set_descricao(descricao)
    prioridade = obj.get_prioridade()
    heapq.heappush(lista_tarefas, (1/prioridade, obj))

def consultar():
    for item in lista_tarefas:
        print (item[1].info())
        print ("-" * 20)

def realizar():
    # a tarefa de "MAIOR" prioridade
    tarefa = heapq.heappop(lista_tarefas)
    print (tarefa[1].info())

if __name__ == '__main__':
    opcao = 1
    while opcao != 4:
        menu()
        opcao = int(input("Digite a opcao desejada: "))
        match opcao:
            case 1:
                adicionar()
            case 2:
                realizar()
            case 3:
                consultar()
            case 4:
                print("Finalizando programa...")
                break
            case _:
                print("Opcao inválida!")
