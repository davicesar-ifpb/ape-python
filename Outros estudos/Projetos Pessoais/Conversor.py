# Mensagem de boas-vindas e explicação do programa
print("Bem-vindo ao Conversor de Peso! (Meu primeiro programa em python.)") #***
print("Este programa converte entre Kilogramas (Kg) e Libras (Lbs).")
print()
# Instruções para o usuário
print("Instruções:")
print("1. Informe o peso na unidade atual (Kg ou Lbs).")
print("2. Escolha para qual unidade deseja converter.")
print()
# Explicação da conversão automática
print("O programa realizará automaticamente a conversão e mostrará o resultado.")
print()
while True:
    ok = input("Digite 'Ok' para continuar ou 'Sair' para fechar o programa: ")

    if ok.upper() == "OK":
        peso = float(input("Peso: "))

        conversaoKg = peso / 2.20462
        conversaoLb = peso * 2.20462

        peso2 = ""
        while peso2 != ("L", "K"):
            peso2 = str(input("(K)g ou (L)bs: "))
            if peso2.upper() == "L":
                print("Peso em Lb: ", conversaoLb)
                break
            elif peso2.upper() == "K":
                print("Peso em Kg: ", conversaoKg)
                break
            else:
                print('Escreva apenas "l" ou "k"')
    
    elif ok.upper() == "SAIR":
        break
    
    else:
        print("Deixe de ser besta")
    
