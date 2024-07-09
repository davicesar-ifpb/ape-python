""" Escreva um programa que, dado um número inteiro representando uma quantidade de
segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade.
Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos. """


segundos_inicial = int(input("Digite a quantiade de segundos: "))
horas = segundos_inicial // 3600
resto = segundos_inicial % 3600
minutos = resto // 60
segundos_final = resto % 60

print(f"{horas} horas, {minutos} minutos, {segundos_final} segundos.")