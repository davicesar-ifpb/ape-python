import random
import os
import time
# Sorteador


def printar_itens(itens):
    print("Itens a serem sorteados:")
    print("-" * 10)
    for i in itens:
        print(i)
    print("-" * 10, "\n")


def sortear(itens):
    item_sorteado = random.choice(list(itens))

    os.system("cls||clear")
    for i in range(1, 4):
        print("Sorteando", "." * i, end="\r", sep="")
        time.sleep(0.5)

    os.system("cls||clear")
    print("Item sorteado:")
    print("-" * 10)
    print(item_sorteado)
    print("-" * 10)
    
    input("Aperte 'enter' para voltar")
    os.system("cls||clear")


def main():
    itens = set()

    while True:
        if itens: printar_itens(itens)

        print("> Digite o nome do item para adicioná-lo aos itens a serem sorteados.")
        print("> Para remover basta digitar o nome novamente.")
        print("> Para sortear aperte 'enter' (deixe vazio).")
        entrada = input("> ").capitalize()

        if not entrada and itens:
            sortear(itens)
            continue
        
        if not entrada and not itens:
            os.system("cls||clear")
            print("Não foi possível sortear, não há nenhum item na lista.\n")
            continue
        
        if entrada in itens:
            itens.remove(entrada)
        else:
            itens.add(entrada)

        os.system("cls||clear")


if __name__ == "__main__":
    main()
