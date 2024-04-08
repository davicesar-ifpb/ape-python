""" Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-
se que nota1 possui peso 6 e nota2 possui peso 4. """


peso1 = 6
peso2 = 4

nota1 = int(input("Digite a nota número 1: "))
nota2 = int(input("Digite a nota número 2: "))

media = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)

print("A média ponderada das notas é:", media)