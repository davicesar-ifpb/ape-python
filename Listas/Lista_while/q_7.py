""" Faça um programa que leia a idade de várias pessoas visitantes de um show (a
leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
• A média de idade do público;
• A porcentagem de pessoas com idade entre 18 e 21 anos;
• Idade do visitante mais jovem. """


qtd_pessoas_idades_18_21 = 0
idades_pessoas = []

while True:

    idade = int(input())

    if idade == 0: break

    if 18 <= idade <= 21:
        qtd_pessoas_idades_18_21 += 1

    idades_pessoas.append(idade)


print(f"Media das idades: {sum(idades_pessoas) / len(idades_pessoas):.0f}")
print(f"Quantidade pessoas entre 18 - 21: {qtd_pessoas_idades_18_21}")
print(f"Pessoa mais nova: {min(idades_pessoas)}")

    