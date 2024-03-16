cidade = 1
while True:
    imoveis = int(input())
    if imoveis == 0:
        break
    
    lista = []
    i = imoveis
    while i > 0:
        pessoa,consumo = [int(x) for x in input().split()]
        lista.append((pessoa,consumo))
        i -= 1
    
    consumos = []
    consumos_ordenar = []
    pessoas = []
    soma_consumos = 0
    soma_pessoas = 0
    for p,c in lista:
        soma_consumos = soma_consumos + c
        soma_pessoas = soma_pessoas + p
        consumo_por_pessoa = c // p
        if consumo_por_pessoa in consumos:      
            sominha = pessoas[consumos.index(consumo_por_pessoa)] + p
            pessoas[consumos.index(consumo_por_pessoa)] = sominha
        else:
            consumos.append(consumo_por_pessoa)
            consumos_ordenar.append(consumo_por_pessoa)
            pessoas.append(p)
    
    consumos_ordenar.sort()
    print(f"Cidade# {cidade}:")
    for c in consumos_ordenar:
        index = consumos.index(c)
        print(f"{pessoas[index]}-{c}",end=" ")
    consumo_medio = soma_consumos / soma_pessoas
    consumo_medio_truncado = int(consumo_medio * 100) / 100
    print(f"\nConsumo medio: {(consumo_medio_truncado):.2f} m3.")
    cidade += 1
