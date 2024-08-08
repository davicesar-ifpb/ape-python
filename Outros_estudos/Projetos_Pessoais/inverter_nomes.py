def inverter_nome(nome):
    a = len(nome)
    b = ""
    while a > 0:
        a -= 1
        b = b + nome[a]
    return b

def inverter2(nome):
    b = ""
    for i in range((len(nome) - 1),-1,-1):
        b = b + nome[i]
    return b

print(f"Seu nome invertido é: {inverter_nome(input('Qual seu nome: '))}")    # | Opção a
print(f"Seu nome invertido é: {inverter2(input('Qual seu nome: '))}")       # | Opção b

#--------------------------------------------------- =/= --------------------------------------------------

# print(f"Seu nome invertido é: {input('Digite seu nome: ')[::-1]}")    | Opção Python




