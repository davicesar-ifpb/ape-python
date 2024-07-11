# Questao 1

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 <= n2 and n1 <= n3:
    soma = n2 + n3
elif n2 <= n1 and n2 <= n3:
    soma = n1 + n3
elif n3 <= n1 and n3 <= n2:
    soma = n1 + n2 
    
media = soma / 2

if media >= 0 and media <= 39:
    conceito = "E"
elif media <= 59:
    conceito = "D"
elif media <= 79:
    conceito = "C"
elif media <= 89:
    conceito = "B"
elif media <= 100:
    conceito = "A"
    
print(media)
print(conceito)
if conceito == "A" or conceito == "B" or conceito == "C":
    print("Aprovado")
else:
    print("Reprovado")