""" Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metros e cresce 3 centímetros por ano. Faça um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico. """


chico = 1.50
ze = 1.10

chico_taxa = 0.02
ze_taxa = 0.03


anos = 0
while chico < ze:
    chico += chico_taxa
    ze += ze_taxa
    anos += 1
print(anos)

