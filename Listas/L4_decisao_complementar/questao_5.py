""" Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os
seus coeficientes. Fórmulas:

Obs: se Δ for negativo, não existem as raízes da equação.
Dica: use a função sqrt do módulo math. """


def raizes(a,b,c):
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print("Não existem raizes da equação.")
    else:
        x1 = (-b + (delta ** 0.5)) / (2*a)
        x2 = (-b - (delta ** 0.5)) / (2*a)
        print(f"X' = {x1}")
        print(f'X" = {x2}')
        
        
a,b,c = map(int, input("Digite, separado por espaços, os coeficientes (a,b,c): ").split())
raizes(a,b,c)