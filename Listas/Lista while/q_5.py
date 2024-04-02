while True:
    n = int(input())

    if n & 1:
        print(f"O número {n} é impar")
    else:
        print(f"O número {n} é par")

    continuar = input("Continuar? (s/n): ")

    if continuar.lower() == "n":
        break


    