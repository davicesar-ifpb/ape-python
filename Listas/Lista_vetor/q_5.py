n = int(input('N = '))
if n == 0:
    print("Nao ha elementos no vetor")
    exit()
    
vetor = [int(input(f"Vetor[{i}] = ")) for i in range(n)]

maior = menor = vetor[0]
indice_maior = indice_menor = 0

for idx, num in enumerate(vetor):
    if num > maior:
        maior = num
        indice_maior = idx
    else:
        menor = num
        indice_menor = idx
            
    
print(f"{maior = }, {indice_maior = }")
print(f"{menor = }, {indice_menor = }")