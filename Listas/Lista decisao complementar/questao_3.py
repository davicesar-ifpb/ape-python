while True:
    ano = int(input("Digite o ano: "))

    if ano % 4 == 0 and ano % 100 != 0:
        print("Ano bissexto")
    elif ano % 100 == 0 and ano % 400 == 0:
        print("Ano bissexto")
    else:
        print("Ano normal")


""" def calc_ano_bissexto(rangeA,rangeB) -> None:
    import json
    
    def mandar_json():
        with open('anos.json', 'w') as f:
            json.dump(anos_dic, f, indent=4)

    anos_dic = {}

    try: # cria um .json se nao existir
        open("anos.json", 'r')
    except FileNotFoundError:
        mandar_json()

    for ano in range(rangeA,rangeB):
        if int(ano) % 4 == 0 and int(ano) % 100 != 0:
            anos_dic.update({str(ano):"ano bissexto"})
            
        elif int(ano) % 100 == 0 and int(ano) % 400 == 0:
            anos_dic.update({str(ano):"ano bissexto"})
            
        else:
            anos_dic.update({str(ano):"ano normal"})
        
    mandar_json()
    print("Dados enviados ao json.")
 """