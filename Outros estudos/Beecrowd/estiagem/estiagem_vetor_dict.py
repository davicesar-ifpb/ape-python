import time

def main():
    cidade = 1
    array = []
    while True:
        imoveis = int(input())
        if imoveis == 0:
            break

        soma_consumos = 0
        consumoS_por_pessoa_dict = {x: 0 for x in range(201)}
        for _ in range(imoveis):
            pessoa, consumo = map(int, input().split())
            soma_consumos += consumo
            consumo_por_pessoa = consumo // pessoa
            consumoS_por_pessoa_dict[consumo_por_pessoa] += pessoa
            
        consumo_medio = int(soma_consumos / sum(consumoS_por_pessoa_dict.values()) * 100) / 100
        
        resultado = ''
        if cidade != 1:
            resultado += f'\n\nCidade# {cidade}:\n'  
        else:
            resultado += f'Cidade# {cidade}:\n'  

        resultado += ''.join(f'{valor}-{chave} ' for chave,valor in consumoS_por_pessoa_dict.items() if valor != 0)
        resultado += f'\nConsumo medio: {consumo_medio} m3.'

        array.append(resultado)
        cidade += 1

    print(''.join(array))


if __name__ == "__main__":
    antes = time.time()
    main()
    depois = time.time()
    print(depois-antes)
