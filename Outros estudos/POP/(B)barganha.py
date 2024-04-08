qtd = int(input())

for casos in range(qtd):
    tamanho = int(input())
    numero = list(x for x in input())
    
    parar = False
    for i in range(len(numero)):
        if parar is True: break
        maior = sorted(numero[i:], reverse=True)[0]
        
        for j in range(len(numero)-1, -1, -1):
            if numero[j] == maior and numero[j] > numero[i]:
                numero[i],numero[j] = numero[j],numero[i]
                parar = True
                break
            
    
    print(f"Caso {casos+1}:","".join(str(x) for x in numero))