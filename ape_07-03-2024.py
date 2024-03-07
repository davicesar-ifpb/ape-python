 frequencia = int(input("Digite a porcetagem de frequencia: "))
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
media_user = (nota1 + nota2) / 2
print(f"Media = {media_user:.1f}")

if frequencia < 75:
    print("Reprovado por falta")
elif media_user >= 70:
    print("aprovado")
elif media_user >= 40:
    print("está na final")
else:
    print("reprovado")