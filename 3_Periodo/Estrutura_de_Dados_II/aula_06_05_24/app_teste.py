from Tarefa import Task

obj = Task("Lavar roupa")
outro = Task("Fazer almoco")

print (obj.get_titulo())
print (outro.get_titulo())
outro.set_descricao ("Descricao do outro objeto")

print (obj.info())
print("-" * 20)
print (outro.info())
