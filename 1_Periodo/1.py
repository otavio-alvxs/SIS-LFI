acumulador = 0
contador = 0
i = 0
while i <= 5:
    i = -1
    if i == 4:
        contador = i
        break
    i = acumulador + 2
    acumulador = acumulador + 1

print ("i", i)
print ("acumulador", acumulador)
print ("contador", contador)
