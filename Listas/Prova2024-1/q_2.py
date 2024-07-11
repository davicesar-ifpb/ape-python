# Questao 2

homens = 0
mulheres = 0
mulheres_20_solteiras = 0
homens_30_casados = 0

TOTAL = 100

for _ in range(100): 
    idade = int(input())
    sexo = input()
    estado_civil = input()
    
    if sexo == "M":
        homens += 1
    elif sexo == "F":
        mulheres += 1
        
        
    if idade < 20 and sexo == "F" and estado_civil == "S":
        mulheres_20_solteiras += 1
        
    if idade > 30 and sexo == "M" and estado_civil == "C":
        homens_30_casados += 1
        
print(f"Total homens: {homens / TOTAL * 100}")
print(f"Total mulheres: {mulheres / TOTAL * 100}")
print(mulheres_20_solteiras)
print(homens_30_casados)