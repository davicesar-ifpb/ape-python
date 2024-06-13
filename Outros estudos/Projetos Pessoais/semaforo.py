import time
import os
from colorama import Fore


def semaforo_original():
    sinais = [
        (Fore.GREEN + "Verde" + Fore.RESET, 10),
        (Fore.YELLOW + "Amarelo" + Fore.RESET, 3),
        (Fore.RED + "Vermelho" + Fore.RESET, 10)
    ]

    while True:
        for cor, tempo in sinais:
            a = False
            while tempo >= 0:
                print(f"{cor}", "[*]" * tempo)
                if a == False:
                    if cor in sinais[1]:
                        time.sleep(1)
                    else:
                        time.sleep(8)
                time.sleep(1)
                tempo -= 1
                os.system('cls||clear')
                a = True


# Outra versao (mais legivel)
def semaforo_novo():
    verde = Fore.GREEN
    amarelo = Fore.YELLOW
    vermelho = Fore.RED

    sinais = {
        "Verde" : {"tempo": 10, 
                    "cor": verde},
        "Amarelo":{"tempo": 3,
                    "cor": amarelo},
        "Vermelho":{"tempo": 10,
                    "cor": vermelho}
    }

    while True:
        for nome_cor, info in sinais.items():
            os.system('cls||clear')
            print(f"{info['cor']}{nome_cor} {'[*]' * info['tempo']}")
            
            if nome_cor == "Amarelo":
                time.sleep(1)
            else:
                time.sleep(8)
    
            for tempo in reversed(range(info['tempo'])):
                os.system('cls||clear')
                print(f"{info['cor']}{nome_cor} {'[*]' * tempo}")
                time.sleep(1)


semaforo_novo()