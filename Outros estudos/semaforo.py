import time
import os
from colorama import init, Fore
init()

sinais = [(Fore.GREEN + "Verde" , 10 ), (Fore. RESET + Fore.YELLOW + "Amarelo", 3), (Fore. RESET + Fore.RED + "Vermelho", 10)]

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
            