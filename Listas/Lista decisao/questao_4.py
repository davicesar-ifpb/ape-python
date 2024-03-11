nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ")

if sexo.upper() == "M":
    print(f"Olá, Sr. {nome}!")
elif sexo.upper() == "F":
    print(f"Olá. Sra. {nome}!")
else:
    print(f"Olá {nome}")