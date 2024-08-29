regra = "AEIOU "

texto = input()
criptografado = ''

for i in texto:
    if i in regra:
        criptografado += regra[::-1][regra.index(i)]
    else:
        criptografado += i

print(criptografado)
