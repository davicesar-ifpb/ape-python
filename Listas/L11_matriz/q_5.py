""" 
Escreva um programa que:
• Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma
turma e a média de cada um deles.
o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
o As médias serão calculadas e armazenadas na 4a coluna da matriz.
• Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
• Calcule e imprima a média geral da turma.
• Calcule e imprima o número de alunos com média superior à média geral da turma.
"""


import random

matriz = [0] * 20

# Preencher matriz
soma_medias = 0
for i in range(20):
    notas = [random.randint(0,100) for _ in range(3)] + [0]
    media = round((sum(notas) / 3), 1)
    notas[3] = media
    soma_medias += media
    matriz[i] = notas

media_geral = round((soma_medias / 20), 1)
acima_media = 0

# Checar alunas acima da media
for i in range(20):
    if matriz[i][-1] > media_geral:
        acima_media += 1

# Exibir matriz
print("[Nota1,Nota2,Nota3,Media]")
print(*matriz, sep='\n')
print("Media geral:", media_geral)
print("Alunos acima da media:", acima_media)