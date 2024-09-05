"""
Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua média e seu
conceito.
O programa deve conter as seguintes funções:
• Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua média
(aritmética).
• Uma função que receba como parâmetro a média do aluno e retorne o seu conceito, de
acordo com a tabela abaixo:

    MÉDIA          CONCEITO
  >= 8,0               A
  >= 5,0 e < 8,0       B
  < 5,0                C
"""

def conceito(a,b,c):
    media = (a+b+c) / 3

    if media < 5:
        return "C"
    
    if media < 8:
        return "B"

    return "A"

n1,n2,n3 = map(float, input("Digite as notas: ").split())

print(conceito(n1,n2,n3))