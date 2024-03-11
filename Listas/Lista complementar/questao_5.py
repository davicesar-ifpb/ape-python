segundos_inicial = int(input("Digite a quantiade de segundos: "))
horas = segundos_inicial // 3600
resto = segundos_inicial % 3600
minutos = resto // 60
segundos_final = resto % 60

print(f"{horas} horas, {minutos} minutos, {segundos_final} segundos.")