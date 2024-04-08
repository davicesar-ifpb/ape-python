""" O cardápio de uma casa de lanches, especializada em sanduíches, é dado a
seguir.
CÓDIGO NOME PREÇO
H Hamburger R$ 5,00
C Cheese Burger R$ 6,00
B Cheese Bacon R$ 7,00
F Cheese Frango R$ 4,00

Faça um programa que leia o código e a quantidade de cada item comprado
por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao
final, calcule e exiba o total a pagar.
Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2
Cheese Bacon:
Entrada:
Código: H
Quantidade: 3
Código: B
Quantidade: 2
Código: X
Saída:
Total a pagar: R$ 29.00 """


precos = {'H': 5.00, 'C': 6.00, 'B': 7.00, 'F': 4.00}

total_pagar = 0.00

while True:
    codigo = input("Código (ou 'X' para sair): ").upper()  
    if codigo == 'X': break  
    
    quantidade = int(input("Quantidade: "))
    if codigo in precos:
        total_pagar += precos[codigo] * quantidade
    else:
        print("Código inválido. Por favor, insira um código válido.")

print(f"Total a pagar: R$ {total_pagar:.2f}")