nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
media_user = (nota1 + nota2) / 2
media_minima = 70
print(f"Media = {media_user:.1f}")

#print("Aprovado") if media_user >= media_minima else print("Reprovado")

if media_user >= media_minima:
    print("Aprovado")
elif media_user >= 40:
    print("Está na final")
else:
    print("Se lascou amigo")