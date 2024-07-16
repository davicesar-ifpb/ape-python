# Questao 3

soma_pares = 0
soma_impares = 0
maior_par = 1 # Nunca vai ser impar, por isso inicializar com valor impar (qualquer valor)
maior_impar = 0 # Nunca vai ser par, por isso inicializar com valor par (qualquer valor)

while True:
    n = int(input())
    
    if n == 0:
        break
    
    # True or False
    par = n % 2 == 0
    
    if par:
        soma_pares += n
        if maior_par == 1:
            maior_par = n
        elif n > maior_par:
            maior_par = n
        
    else:
        soma_impares += n
        if maior_impar == 0:
            maior_impar = n
        elif n > maior_impar:
            maior_impar = n
            
print(soma_impares)
print(soma_pares)

if maior_impar == 0:
    print("Não houve impares")
else:
    print(maior_impar)

if maior_par == 1:
    print("Não houve pares")
else:
    print(maior_par)

    