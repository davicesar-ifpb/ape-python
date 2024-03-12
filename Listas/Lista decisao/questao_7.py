altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

# Calculos -------------
imc = peso / altura ** 2
pesoMaximoNormal = 24.9 * altura ** 2
pesoMinimoNormal = 18.5 * altura ** 2
perderKg = peso - pesoMaximoNormal
ganharKg = pesoMinimoNormal - peso
# ----------------------

print(f"\nImc: {imc:.2f}")
if imc < 18.5:
    print("** Baixo peso **")
    print(f"Para atingir o imc normal é necessário pesar {pesoMinimoNormal:.2f}kg")
    print(f"ou ganhar {ganharKg:.2f}kg")
elif imc >= 18.5 and imc < 25:
    print("Normal :)")
elif imc >= 25 and imc < 30:
    print("** Sobrepeso **")
    print(f"Para atingir o imc normal é necessário pesar {pesoMaximoNormal:.2f}kg")
    print(f"ou perder {perderKg:.2f}kg")
else:
    print("** Obesidade **")
    print(f"Para atingir o imc normal é necessário pesar {pesoMaximoNormal:.2f}kg")
    print(f"ou perder {perderKg:.2f}kg")