import time
import os
from colorama import Fore


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

