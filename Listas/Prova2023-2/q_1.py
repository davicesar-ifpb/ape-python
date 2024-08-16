""" Escreva um programa que:
• Leia um valor inteiro N;
• Leia um vetor A contendo N inteiros;
• Gere e imprima um vetor B onde cada elemento de B será calculado com base no elemento de A
da mesma posição usando a seguinte regra: se o elemento de A for par, o elemento de B será 0,
e se o elemento de A for ímpar, o elemento de B será 1.
Exemplo: N = 8, A = [7, 12, 15, 10, 4, 9, 3, 6], B = [1, 0, 1, 0, 0, 1, 1, 0] """

n = int(input("Digite o tamanho do vetor: "))

vetor_A = [int(input(f"Vetor [{x}]: ")) for x in range(n)]
#vetor_A = list(map(int, input().split()))

vetor_B = [0 if x % 2 == 0 else 1 for x in vetor_A]

# Forma mais simples de fazer
# vetor_B = []
# for i in vetor_A:
#     if i % 2 == 0:
#         vetor_B.append(0)
#     else:
#         vetor_B.append(1)

print()
print(vetor_A)
print(vetor_B)