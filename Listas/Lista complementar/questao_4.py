""" Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
bem como o número de litros de combustível gastos.
Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a
capacidade do tanque e mostre:
a) Quilometragem rodada.
b) Quantos quilômetros por litro faz o veículo.
c) Autonomia do veículo.
d) Custo da viagem. """


hodometro_antes = int(input("Hodometro antes: "))
hodometro_depois = int(input("Hodometro depois: "))
combustivel_gasto = int(input("Combustivel gasto: "))
preco_litro = float(input("Preco do litro: "))
capacidade = int(input("Capacidade do tanque: "))

quilometragem = hodometro_depois - hodometro_antes
kmL = quilometragem / combustivel_gasto
autonomia = capacidade * kmL
custo = combustivel_gasto * preco_litro

print(f"Quilometragem rodada: {quilometragem} km")
print(f"Quilometros por litro: {kmL:.2f} km/L")
print(f"Autonomia: {autonomia:.2f} km")
print(f"Custo da viagem: R${custo}")