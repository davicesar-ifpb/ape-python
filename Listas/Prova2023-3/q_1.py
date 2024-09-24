def quantidade_ocorrencias(matriz, valor):
    qtd = 0
    
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])): 
            if matriz[i][j] == valor:
                qtd += 1

    return qtd

def quantidade_ocorrencias2(matriz, valor):
    qtd_ocorrencias = 0
        
    for linha in matriz:
        qtd_por_linha = linha.count(valor)
        qtd_ocorrencias += qtd_por_linha
    
    return qtd_ocorrencias


# Testes
matriz1 = [[2, 2, 5], 
           [4, 5, 6],    # 3 occorencias (5)
           [1, 5, 9]]

matriz2 = [[1, 2, 1],
           [2, 5, 6],   # 2 occorencias (5)
           [7, 8, 9],
           [0, 1, 5]]

matriz3 = [[1, 2, 3], 
           [4, -1, 1],  # 0 occorencias (5)
           [7, 0, 2], 
           [9, 1, 2], 
           [0, 4, 6]]

print(quantidade_ocorrencias(matriz1, 5))
print(quantidade_ocorrencias(matriz2, 5))
print(quantidade_ocorrencias(matriz3, 5))