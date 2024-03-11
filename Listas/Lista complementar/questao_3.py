var1 = input("Digite algo para a variável 1: ")
var2 = input("Digite algo para a variável 2: ")
print(f"Variável 1: {var1}\nVariável 2: {var2}")
temp = var2
var2 = var1
var1 = temp
print("Trocando>")
print(f"Variável 1: {var1}\nVariável 2: {var2}")