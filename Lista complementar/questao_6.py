dinheiroInicial = int(input("Digite o seu saldo em B$: "))

cinquenta = dinheiroInicial // 50
resto50 = dinheiroInicial % 50
dez = resto50 // 10
resto10 = resto50 % 10
cinco = resto10 // 5
resto5 = resto10 % 5
um = resto5 // 1

print(f"{cinquenta} nota de B$50\n{dez} notas de B$10\n{cinco} notas de B$5\n{um} nota de B$1")
