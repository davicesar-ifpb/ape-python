operacao = input("Selecione a operação\n(+ - x * / %): ")
num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
match operacao:
    
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "x"|"*":
        print(f"{num1} * {num2} = {num1 * num2}")
    
    case "/":
        if num2 == 0:
            print("Divisão por 0.")
        else:
            print(f"{num1} - {num2} = {num1 - num2}")
    
    case "%":
        print(f"{num1} % {num2} = {num1 * (num2 / 100)}")
    
    case _:
        print("Operador desconhecido.")