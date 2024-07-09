nivel_suspeita = 0

perguntas = [
    "Telefonou para a vitima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou para a vítima? "
]

for pergunta in perguntas:
    resposta = input(pergunta).upper()

    if resposta == "S":
        nivel_suspeita += 1

if nivel_suspeita < 2:
    print("Inocente")

elif nivel_suspeita == 2:
    print("Suspeito")

elif nivel_suspeita <= 4:
    print("Cúmplice")

else:
    print("Assassino")
