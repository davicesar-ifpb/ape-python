"""
Escreva uma função chamada vertical que receba como parâmetro uma string e
a exiba na vertical, ou seja, com uma letra em cada linha. Faça também um
programa para testar a função.
"""

def vertical(s: str) -> None:
    """
    Recebe string e a printa na vertical
    """
    for i in s:
        print(i)


string = input("digite uma string pfv")
vertical(string)