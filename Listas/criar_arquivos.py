import os

quantidade_de_arquivos = 5

for i in range(1, quantidade_de_arquivos+1):
    filename = f'q_{i}.py'
    diretorio = os.path.dirname(__file__) + f'\\{filename}'
    with open(diretorio, 'w') as f:
        print(f"{filename} criado")