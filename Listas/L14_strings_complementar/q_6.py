verbo = input()

pronomes = ["Eu", "Tu", "Ele", "Nós", "Vós", "Eles"]

ar = ["o", "as", "a", "amos", "ais", "am"]
er = ["o", "es", "e", "emos", "eis", "em"]
ir = ["o", "es", "e", "imos", "is", "em"]

print()
if verbo[-2:] == "ar":
    for idx, i in enumerate(ar):
        print(pronomes[idx], verbo[:-2] + i)

elif verbo[-2:] == "er":
    for idx, i in enumerate(er):
        print(pronomes[idx], verbo[:-2] + i)

elif verbo[-2:] == "ir":
    for idx, i in enumerate(ir):
        print(pronomes[idx], verbo[:-2] + 1)

else:
    print("Não é um verbo regular")