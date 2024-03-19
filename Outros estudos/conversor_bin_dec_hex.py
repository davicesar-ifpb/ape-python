import os
bases = {"10":"decimal", "2":"binario", "16":"hexadecimal"}


def binario_hexa(numero) -> str:         # ---------- binario-hexa
    if base_inicial == "binario":
        numero_decimal = int(numero, 2)
        numero_convertido = hex(numero_decimal)[2:]         
    else:
        numero_decimal = int(numero, 16)
        numero_convertido = bin(numero_decimal)[2:]
    return numero_convertido           
        

def binario_decimal(numero) -> str:      # ---------- binario-decimal
    if base_inicial == "binario":     
        numero_convertido = int(numero, 2)    
    else:
        numero_convertido = bin(int(numero))[2:]
    return numero_convertido
        

def decimal_hexa(numero) -> str:         # ---------- decimal-hexa
    if base_inicial == "decimal":
        return hex(int(numero))[2:]
    else:
        return int(numero, 16)


def qual_base(texto):
    while True:
        entrada = input(texto)
        if entrada in ("hex","hexa"):
            base_inicial_ou_final = "hexadecimal"
            break
        
        if entrada in bases or entrada in bases.values():
            base_inicial_ou_final = bases.get(entrada)
            if base_inicial_ou_final == None:
                base_inicial_ou_final = entrada
            break          
        else:
            os.system("cls")
            print(f"Erro. Bases disponíveis: [decimal (10) / binario (2) / hexadecimal (16)]")
    
    return base_inicial_ou_final


while True:
    base_inicial = qual_base("De qual base é o número que você quer converter? ")
    base_final = qual_base("Para qual base você quer converter? ")
    numero = input("Digite o número: ")

    try:
        os.system("cls")
        if base_inicial == base_final:
            print(f"Número digitado = Número convertido -> {base_inicial}: {numero}")
        
        elif (base_inicial == "binario" and base_final == "hexadecimal") or (base_final == "binario" and base_inicial == "hexadecimal"):
            print(f"Número digitado -> {base_inicial}: {numero}\nConvertido -> {base_final}: {binario_hexa(numero)}")

        elif (base_inicial == "binario" and base_final == "decimal") or (base_final == "binario" and base_inicial == "decimal"):
            print(f"Número digitado -> {base_inicial}: {numero}\nConvertido -> {base_final}: {binario_decimal(numero)}")

        else:
            print(f"Número digitado -> {base_inicial}: {numero}\nConvertido -> {base_final}: {decimal_hexa(numero)}")
        
        break
    
    except ValueError:
        os.system("cls")
        print("Número escolhido não corresponde à base selecionada.")
