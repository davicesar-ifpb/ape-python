""" Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que leia um número e determine se ele é ou não
primo. """


def primos_n_unico_1(entrada: int):
    #entrada = int(input())
    for i in range(1,entrada+1):
        if entrada == 1:
            print("Não é primo")
            break   
        if entrada % i == 0 and entrada == i:
            print("É primo")
            break
        elif entrada % i == 0 and i < entrada and i != 1:
            print("Não é primo")
            break
    
def primos_n_unico_2(entrada: int):
    #entrada = int(input())
    if entrada == 2:
        print("É primo")
    elif entrada % 2 == 0:
        print("Não é primo")
    else:
        for i in range(3,entrada,2):
            q = entrada // i
            
            if i > q and entrada % i != 0:
                print("É primo")
                break
            elif entrada % i == 0:
                print("Não é primo")
                break

def primos_todos(quantidade: int):
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
                

import time,os

inicio = time.time()
primos_todos(50000)
fim = time.time()
os.system("cls")
Primos1 = fim - inicio

print(f"{Primos1 = }")
