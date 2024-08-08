import random


def gerar_numeros_aleatorios(j: int, k: int, n: int) -> list:
    return [str(random.randint(j, k)) + "\n" for _ in range(n)]


def escrever_numeros_aleatorios(arquivo: str, numeros: list):
    with open(arquivo, "w") as file:
        file.writelines(numeros)


def randomizer(intervalo_0: int, intervalo_1: int, qtd_numeros: int, arquivo: str):
    numeros = gerar_numeros_aleatorios(intervalo_0, intervalo_1, qtd_numeros)
    escrever_numeros_aleatorios(arquivo, numeros)
    

if __name__ == "__main__":
    randomizer(1, 10, 20, "input.txt")
