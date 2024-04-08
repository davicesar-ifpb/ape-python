""" Faça um programa que, para um grupo de N pessoas (obs: N será lido):
• Leia o sexo (M ou F) de cada pessoa;
• Calcule e escreva o percentual de homens;
• Calcule e escreva o percentual de mulheres. """


entrada = int(input("Digite a quantidade de pessoas: "))

femeas = 0
machos = 0
for i in range(entrada):
    while True:
        sexo = input("Digite o sexo (M/F): ")
        if sexo in "mM":
            machos += 1
            break
        elif sexo in "fF":
            femeas += 1
            break
        else:
            print('Sexo invalido.')

percentual_femeas = femeas / (femeas + machos) * 100
percentual_machos = machos / (femeas + machos) * 100

print(f"\nMulheres = {percentual_femeas:.1f} %")
print(f"Homens = {percentual_machos:.1f} %")