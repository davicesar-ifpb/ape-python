numeros = []

while len(numeros) < 6:
    n = int(input())

    if n in numeros:
        print("Repetido")
        continue
    
    numeros.append(n)
    

print(numeros)
