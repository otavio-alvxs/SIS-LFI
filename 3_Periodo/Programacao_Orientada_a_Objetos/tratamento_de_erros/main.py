try:
	with open ('arquivo.txt', 'r') as file_object:
		texto = file_object.read()
		print (texto)
except Exception as e:
	print ("Fudeu mayko")
