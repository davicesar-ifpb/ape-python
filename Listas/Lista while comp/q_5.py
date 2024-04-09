""" Faça um programa que, leia a temperatura dos 30 dias do mês de abril diga
qual o dia mais quente e o dia mais frio do mês (obs: suponha que não haja
empates). """


temperatura = int(input("Temperatura dia 1: "))
mais_frio = temperatura
dia_mais_frio = 1
mais_quente = temperatura
dia_mais_quente = 1

for i in range(2,31):
    temperatura = int(input(f"Temperatura dia {i}: "))
    if temperatura > mais_quente:
        mais_quente = temperatura
        dia_mais_quente = i
    if temperatura < mais_frio:
        mais_frio = temperatura
        dia_mais_frio = i
        
print(f"Dia mais frio: {dia_mais_frio} ({mais_frio}°C)")
print(f"Dia mais quente: {dia_mais_quente} ({mais_quente}°C)")