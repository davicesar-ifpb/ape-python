dia, mes, ano = input().split("/")

nome = input().split()

nome_formatado = nome[0].capitalize() + nome[-1].capitalize()

indentificador = f'{ano}{mes}{dia}_{nome_formatado}'

print(indentificador)


# Se quiser criar uma função --------------------------------------------


def indentificador(data:str, nome:str):
    dia,mes,ano = data.split("/")
    nome = nome.split()
    nome_formatado = nome[0].capitalize() + nome[-1].capitalize()
    indentificador = f'{ano}{mes}{dia}_{nome_formatado}'
    
    return indentificador


data = input()
nome = input()
print(indentificador(data, nome))