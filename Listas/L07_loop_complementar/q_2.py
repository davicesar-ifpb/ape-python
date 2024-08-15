""" Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que mostre todos os números primos de 1 a N
(obs: N será lido). """


def primos(quantidade: int):
    for i in range(1,quantidade+1):
        if i == 2 or i == 3:
            print(f"{i} É primo")
        elif i % 2 == 0 or i == 1:
            print(f"{i} Não é primo")
        else:
            for j in range(3,i,2):
                q = i // j
                
                if j > q and i % j != 0:
                    print(f"{i} É primo")
                    break
                elif i % j == 0:
                    print(f"{i} Não é primo")
                    break
        
n = int(input("Valor de N: "))
primos(n)