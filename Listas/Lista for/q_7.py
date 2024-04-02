# Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
# próprio. Faça um programa que leia um número e determine se ele é ou não
# primo.

entrada = int(input())
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
    

# printa todos os numeros primos equivalentes a quantidade escolhida
def primos(quantidade):
    j = 1    
    while j <= quantidade:
        for i in range(1,j+1):
            if j == 1:
                print(f"{j} Não é primo")
                break
            
            if j % i == 0 and j == i:
                print(f"{j} É primo")
                break
            elif j % i == 0 and i < j and i != 1:
                print(f"{j} Não é primo")
                break
        j += 1
        
primos(50)