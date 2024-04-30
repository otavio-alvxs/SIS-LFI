import heapq

lista = []

heapq.heappush(lista, (5, "Gerson"))
heapq.heappush(lista, (7, "Clodoaldo"))
heapq.heappush(lista, (1, "Creonilso"))
heapq.heappush(lista, (3, "Tiburcio"))

print ("ATENDIMENTOS")

for i in range(4):
    elemento = heapq.heappop(lista)
    print(elemento)
    input("proximo ")
