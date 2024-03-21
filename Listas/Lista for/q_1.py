# Faça um programa que calcule e mostre os números múltiplos de 5 do
# intervalo 50 a 300, juntamente com suas raízes e seus cubos.

for i in range(50,301,5):
    raiz = f"{i ** (1/2):.2f}"
    print(f"{i: >3} | raiz = {raiz: <5} | cubo = {i ** 3}")