qtd_casos = int(input())

for i in range(qtd_casos):
    
    tamanho_da_fase = int(input())
    fase = input()
    
    amarelinho = fase.index("A")
    pintadinha = fase.index("P")
    carijo = fase.index("C")
    
    
    if "X" in range(amarelinho,pintadinha) or "X" in range(pintadinha,amarelinho):
        distancia_a_p = tamanho_da_fase
    else:
        distancia_a_p = abs(amarelinho - pintadinha)


    if "X" in range(amarelinho,carijo) or "X" in range(carijo, amarelinho):
        distancia_a_c = tamanho_da_fase
    else:
        distancia_a_c = abs(amarelinho - carijo)
        
    
    if distancia_a_c < distancia_a_p:
        print(f"C {distancia_a_c}")
    elif distancia_a_c > distancia_a_p:
        print(f"P {distancia_a_p}")
    else:
        print("FUGIU!")
        
   
