""" Uma certa empresa pretende verificar se os seus empregados estarão
qualificados ou não para aposentadoria em 2025.
Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
• Ter no mínimo 65 anos de idade; ou
• Ter trabalhado no mínimo 30 anos; ou
• Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
Com base nas informações acima, faça um programa para:
• Ler o nome do empregado, o ano de nascimento e o ano de seu ingresso
na empresa.
• Calcular e exibir a idade e o tempo de trabalho do empregado (estimado
ao final de 2024)
• Exibir a mensagem “Pode Requerer Aposentadoria” se atender aos
requisitos ou “Não Pode Requerer Aposentadoria” caso contrário.
Ao final de cada execução, o programa deverá perguntar se o usuário deseja
fazer nova verificação. Se sim, o programa deverá repetir tudo novamente,
caso contrário deverá encerrar. """


import os
while True:
    nome = input("Digite o nome do empregado: ")
    ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
    ano_ingresso = int(input("Digite o ano de ingresso do empregado: "))
    idade = 2024 - ano_nascimento
    tempo_trabalho = 2024 - ano_ingresso
    
    if (idade >= 65) or (tempo_trabalho >= 30) or (idade >= 60 and tempo_trabalho >= 25):
        print("Pode requerer aposentadoria.")
    else:
        print("Não pode requerer aposentadoria.")
    
    repetir = input("Deseja fazer nova verificação? (s/n): ").lower()
    if repetir == "n": 
        break
    os.system("cls||clear")
    
