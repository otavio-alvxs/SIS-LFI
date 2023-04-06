"""A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
∆t: variação de tempo (tempo final – tempo inicial) em horas
Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  
"""
dS = float(input('Variação de espaço (ponto de chegada - ponto de partida) em km:  '))
dt = float(input('Variação de tempo (tempo inicial - tempo final) em horas: '))
vm = dS / dt
print (f'A velocidade média do veículo é de {vm:.2f}')
