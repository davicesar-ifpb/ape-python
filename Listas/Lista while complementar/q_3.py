""" O algoritmo de Euclides para determinar o MDC entre dois números inteiros
consiste em formar uma sequência de inteiros cujos dois primeiros
elementos são os números dados. Cada elemento seguinte é o resto da
divisão dos dois anteriores. A sequência terminará quando um elemento dela
for nulo. O MDC entre os números dados é o elemento anterior ao zero. Faça
uma implementação deste programa.
Ex: Dados os números 12 e 15, será formada a sequência: 12, 15, 12, 3, 0 e o
MDC entre 12 e 15 é 3. """


a,b = map(int, input().split())

print(a,b, sep=" ", end=" ")

mdc = 0
while True:
    c = a % b
    if c == 0: break
    
    mdc = c
    print(c, end=" ")
    a,b = b,c
    
print(0)
print("MDC:",mdc)
