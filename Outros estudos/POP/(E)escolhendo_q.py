qtd = int(input())
provas = input()

casos_3_diferentes = 0

for i in range(qtd-2):
    if provas[i] != provas[i+1] and provas[i] != provas[i+2] and provas[i+1] != provas[i+2]:
        casos_3_diferentes += 1
        
print(casos_3_diferentes/(qtd-2))