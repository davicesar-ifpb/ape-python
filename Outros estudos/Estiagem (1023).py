cidade = 1
while True:
    imoveis = int(input())
    if imoveis == 0:
        break
    
    lista = []
    soma_consumos = 0
    soma_pessoas = 0
    i = imoveis
    z = -1
    while i > 0:
        pessoa,consumo = map(int, input().split())
        soma_consumos = soma_consumos + consumo
        soma_pessoas = soma_pessoas + pessoa
        consumo_por_pessoa = consumo // pessoa
        lista.append((consumo_por_pessoa,pessoa))
        if z >= 0:
            if consumo_por_pessoa == lista[z][0]:
                consumo_novo = lista[z][0]
                pessoa_novo = lista[z][1] + pessoa
                lista.pop()
                lista.pop()
                lista.append((consumo_novo,pessoa_novo))
            else:
                z += 1
        else:
            z += 1
        i -= 1
    
    lista.sort()
    consumo_medio = soma_consumos / soma_pessoas
    consumo_medio_truncado = int(consumo_medio * 100) / 100
    print(f"Cidade# {cidade}:")
    for c,p in lista:
        print(f"{p}-{c}",end=" ")
    print(f"\nConsumo medio: {(consumo_medio_truncado):.2f} m3.")
    cidade += 1
