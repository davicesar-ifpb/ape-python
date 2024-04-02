precos = {'H': 5.00, 'C': 6.00, 'B': 7.00, 'F': 4.00}

total_pagar = 0.00

while True:
    codigo = input("Código (ou 'X' para sair): ").upper()  
    if codigo == 'X':
        break  
    quantidade = int(input("Quantidade: "))
    if codigo in precos:
        total_pagar += precos[codigo] * quantidade
    else:
        print("Código inválido. Por favor, insira um código válido.")

print(f"Total a pagar: R$ {total_pagar:.2f}")