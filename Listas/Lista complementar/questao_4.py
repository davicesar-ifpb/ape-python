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