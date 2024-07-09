""" Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve
solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado
da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir
"Operador desconhecido". """


while True:
    num1, operacao, num2 = input("Digite a expressão usando os operadores: (+|-|*|x|^|%): ").split()
    num1 = float(num1)
    num2 = float(num2)

    match operacao:
        
        case "+":
            print(f"{num1 + num2 = }")
        case "-":
            print(f"{num1 - num2 = }")
        case "x"|"*":
            print(f"{num1 * num2 = }")
        case "^": 
            print(f"{num1} ^ {num2} = {num1 ** num2}")
        case "/":
            if num2 == 0:
                print("Divisão por 0.")
            else:
                print(f"{num1 / num2 = }")
        
        case "%":
            print(f"{num1} % {num2} = {num1 * (num2 / 100)}")
        
        case _:
            print("Operador desconhecido.")


