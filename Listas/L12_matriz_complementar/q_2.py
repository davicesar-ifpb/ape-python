""" Uma matriz quadrada contendo valores inteiros é denominada quadrado
mágico quando a soma dos elementos de cada linha, a soma dos elementos
de cada coluna e a soma dos elementos das diagonais principal e secundária
são todos iguais. Por exemplo, a matriz seguinte é um quadrado mágico. """

ordem = 3

matriz = [0] * ordem

for i in range(ordem):
    matriz[i] = list(map(int, input(f"Linha {i}: ").split()))
    
soma_modelo = sum(matriz[0])
soma_diag_p = 0
soma_diag_s = 0

for i in range(ordem):
    quadrado_magico = True
    soma_coluna = 0
    for j in range(ordem):
        
        if sum(matriz[i]) != soma_modelo:
            quadrado_magico = False
            break
        
        if i == j:
            soma_diag_p += matriz[i][j]
        
        if (i + j) == (ordem - 1):
            soma_diag_s += matriz[i][j]
            
        soma_coluna += matriz[j][i]
        
    if not quadrado_magico:
        break
    
    if soma_coluna != soma_modelo:
        quadrado_magico = False
        break

if soma_diag_p != soma_modelo or soma_diag_s != soma_modelo:
    quadrado_magico = False
    
if quadrado_magico:
    print("\nÉ um quadrado mágico")
else:
    print("\nNão é um quadrado mágico")