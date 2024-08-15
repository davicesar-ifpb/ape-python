""" Um dado material radioativo perde metade de sua massa a cada 50
segundos. Faça um programa que leia uma certa quantidade de massa, em
gramas, deste material e imprima o tempo necessário para que sua massa
se torne menor que 0.5g. """


def meia_vida(g: float) -> str:
    tempo = 0
    
    while g > 0.5:
        g /= 2
        tempo += 50
    
    print(f"{tempo//60}m {tempo%60}s")
        

g = float(input("Massa em g: "))
meia_vida(g)