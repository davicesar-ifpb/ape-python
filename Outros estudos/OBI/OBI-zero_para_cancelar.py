numero_final = []

n = int(input())

for i in range(n):
    e = int(input())
    if e == 0:
        numero_final.pop()
    else:
        numero_final.append(e)
        
# soma = 0
# for i in numero_final:    <--- funciona, mas é lento
#     soma += i
# print(soma)

soma = sum(numero_final)
print(soma)