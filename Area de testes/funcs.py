def drobo():
    while True:
        num = int(input("Digite um número inteiro ou 0 para parar: "))

        if num == 0:
            return print("Fim do programa")

        dobro = num * 2
        print(f"{dobro = }")


def cubo():
    while True:
        num = int(input("Digite um número inteiro ou 0 para parar: "))

        if num == 0 :
            return print("Fim do programa")

        cubo = num ** 2
        print(f"{cubo = }")

def oddOrEven():
    e = int(input("Digite a quantidade de numeros: "))

    for _ in range(e):
        n = int(input("Digite um número inteiro: "))

        if n == 0:
            return print("Fim do programa")

        if n % 2 == 0:
            print("É par man")
        else:
            print("É impar man")

    


def main():
    print("Dobro de um número")
    drobo()

    print("\nCubo de um número")
    cubo()

    print("\nVerificar se um número é par ou impar")
    oddOrEven()

if __name__ == "__main__":
    main()
