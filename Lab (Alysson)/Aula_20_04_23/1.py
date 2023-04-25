massa = float(input('Digite seu peso (em quilos): '))
altura = float(input('Digite sua altura (em metros): '))

imc = massa / (altura ** 2)

print (f'Seu IMC é: {imc}')

if imc < 18.5:
    print ('Você está abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print ('Você está saudável.')
elif imc >= 25 and imc < 30:
    print ('Você está acima do peso.')
elif imc >= 30 and imc < 35:
    print ('Obesidade grau 1.')
elif imc >= 35 and imc < 40:
    print ('Obesidade grau 2.')
elif imc >= 40:
    print ('Obesidade grau 3.')
else:
    print ('IMC inválido.')
