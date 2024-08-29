vogais = "aeiouAEIOU"

n = int(input())
frase = input()
nova_frase = ''

for i in frase:
    if i in vogais:
        nova_frase += i * n
    else:
        nova_frase += i

print(nova_frase)