import time

def main():
    cidade = 1
    array = []
    while True:
        imoveis = int(input())
        if imoveis == 0:
            break

        soma_consumos = 0
        consumoS_por_pessoa_list = [0] * 201  # Usando lista ao invés de dicionário
        for _ in range(imoveis):
            pessoa, consumo = map(int, input().split())
            soma_consumos += consumo
            consumo_por_pessoa = consumo // pessoa
            consumoS_por_pessoa_list[consumo_por_pessoa] += pessoa
            
        consumo_medio = int(soma_consumos / sum(consumoS_por_pessoa_list) * 100) / 100

        resultado = f'Cidade# {cidade}:\n' if cidade == 1 else f'\n\nCidade# {cidade}:\n'
        resultado += ''.join(f'{valor}-{chave} ' for chave, valor in enumerate(consumoS_por_pessoa_list) if valor != 0)
        resultado += f'\nConsumo medio: {consumo_medio} m3.'

        array.append(resultado)
        cidade += 1

    print(''.join(array))


if __name__ == "__main__":
    antes = time.time()
    main()
    depois = time.time()
    print(depois - antes)
