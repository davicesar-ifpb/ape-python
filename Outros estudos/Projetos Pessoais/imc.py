while True:
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso / (altura ** 2)
    
    faixas = [18.5, 24.9, 29.9, 34.9, 39.9]
    rotulos = ["Magreza", "Normal", "Sobrepeso", "Obesidade grau I", "Obesidade grau II"]
    for i,_ in enumerate(faixas):
        if imc < faixas[i]:
            print(f"Seu IMC é: {imc:.2f} -> {rotulos[i]}\n")
            break
    else:
        print(f"Seu IMC é: {imc:.2f} -> Obesidade grau III\n")
        