numeros = [6,7,13,14,26]


for _ in range(20):
    qtd_acertados = 0
    dezenas = []
    
    while len(dezenas) < 8:
        numero = int(input())
        
        if numero in numeros:
            qtd_acertados += 1
            continue

        if numero in range(1, 81) and numero not in dezenas:
            dezenas.append(numero)


print(qtd_acertados)