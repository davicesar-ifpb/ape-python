def p_a(n_inicial,razao,n_termos):
    x = 1
    i = n_inicial
    while i < n_inicial + n_termos * razao:
        print(f"{x}: {i:.2f}")
        x += 1
        i += razao
    termo_central = (n_inicial + (n_termos - 1) * razao + n_inicial) / 2
    print(f"Termo central: {termo_central:.2f}")

print("Para calcular a p.a, é necessário escolher o número inicial, a razão e a quantidade de termos.")
print()
x = float(input("Qual o número inicial: "))
y = float(input("Qual a razão: "))
z = int(input("Quantos termos: "))

p_a(x,y,z)