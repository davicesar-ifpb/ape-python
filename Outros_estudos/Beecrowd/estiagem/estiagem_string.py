import time

def main():
    cidade = 1

    resultado = ''
    while True:
        imoveis = int(input())
        if imoveis == 0:
            break

        qtd_pessoas = 0
        soma_consumos = 0
        consumoS_por_pessoa_dict = {}
        for _ in range(imoveis):
            pessoa, consumo = map(int, input().split())
            qtd_pessoas += pessoa
            soma_consumos += consumo
            consumo_por_pessoa = consumo // pessoa
            if consumo_por_pessoa in consumoS_por_pessoa_dict:
                consumoS_por_pessoa_dict[consumo_por_pessoa] += pessoa
            else:
                consumoS_por_pessoa_dict[consumo_por_pessoa] = pessoa

        
        consumoS_por_pessoa_dict = dict(sorted(consumoS_por_pessoa_dict.items()))
        consumo_medio_str = f'{soma_consumos / qtd_pessoas:.4f}'
        index = consumo_medio_str.index(".") # Onde está o ponto
        consumo_medio = consumo_medio_str[0:index+3] # Duas casas após o ponto sem arredondar (fatia)
        
        if cidade != 1:
            resultado += f'\n\nCidade# {cidade}:\n'  
        else:
            resultado += f'Cidade# {cidade}:\n'  

        resultado += ''.join(f'{consumoS_por_pessoa_dict[i]}-{i} ' for i in consumoS_por_pessoa_dict)
        resultado += f'\nConsumo medio: {consumo_medio} m3.'

        cidade += 1

        print(resultado)


if __name__ == "__main__":
    inicio = time.time()
    main()
    fim = time.time()
    print(fim-inicio)
