""" Faça um programa que solicite ao usuário uma senha. Caso a senha digitada
esteja correta, o programa deverá mostrar senha correta. Caso contrário, o
programa deverá mostrar senha incorreta e pedir para o usuário tentar
novamente digitar a senha correta. Mas, se o usuário fornecer três senhas
incorretas, o programa deverá encerrar a sua execução. (Obs: a senha correta
é “abcd”). """


senha = "abcd"

tentativas = 3
while tentativas > 0:
    tentativa = input()
    
    if tentativa == senha:
        print("Senha correta")
        break
    else:
        print("Senha incorreta")
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}")
        