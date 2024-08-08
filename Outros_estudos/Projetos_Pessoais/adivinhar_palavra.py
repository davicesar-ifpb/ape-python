import re, os, random
  
paises = ["alemanha","angola","argelia","argentina","armenia","australia",
          "belgica","bermudas","bolivia","brasil","camaroes","canada","catar",
          "chile","china","colombia","croacia","cuba","dinamarca","equador",
          "espanha","estadosunidos","finlandia","franca","grecia","india",
          "indonesia","italia","japao","mexico","moruega","paraguai","peru",
          "polinia","portugal","russia","servia","tailandia","turquia","ucrania",
          "uruguai","venezuela"]

animais = ["cachorro", "gato", "elefante", "leao", "tigre", "girafa", "zebra",
           "macaco", "cobra", "jacare", "pinguim", "baleia", "golfinho", "orangotango",
           "rinoceronte", "urso", "hipopotamo", "aguia", "cavalo", "coelho"]

def abrir_arquivo():
    try:
        with open('palavras.txt', 'r') as arquivo:
            lista_de_palavras = arquivo.readlines()
            lista_de_palavras = [l.strip() for l in lista_de_palavras]
    
    except FileNotFoundError:
        with open('palavras.txt', 'w') as arquivo:
            print("Arquivo criado com o nome 'palavras.txt'")
            lista_de_palavras = []
    
    return lista_de_palavras

def cadastrar_palavras():
    while True:
        print("Qual tema você deseja?")
        print("1) Paises\n2) Animais\n3) Escrever manualmente\n4) Sair")
        escolha = input("> ")
        match escolha:
            case "4":
                return
            case "1":
                lista_cadastro = paises
            case "2":
                lista_cadastro = animais
            case "3":
                print("Digite as palavras que quer adicionar ao arquivo separadas por espaço ou 'sair' para voltar")
                lista_cadastro = input("> ").split()
                if 'sair' in lista_cadastro:
                    os.system("cls||clear")
                    continue
        break
        
    with open("palavras.txt", 'w') as f:
        f.writelines(x + "\n" for x in lista_cadastro)
    

def printar_estatisticas(letras_tentadas, tentativas, palavra_formatada):
    if letras_tentadas: 
        print("Letras tentadas:", end=' ')
        print(*letras_tentadas, sep=" | ")
    print(f'Tentativas: {tentativas}')
    print(f'Palavra: {palavra_formatada}')


def main():
    lista_de_palavras = abrir_arquivo()           
    
    if not lista_de_palavras:
        print('palavras.txt está vazio..')
        cadastrar_palavras()
        lista_de_palavras = abrir_arquivo()

    if lista_de_palavras:
        while True: # Jogar novamente
            
            while True: # Cadastrar palavras ou iniciar jogo
                os.system("cls||clear")
                print("Para começar o jogo digite (1)\nPara mudar as palavras digite (2)")
                escolha = input()
                
                if escolha == "2":
                    os.system("cls||clear")
                    cadastrar_palavras()
                    lista_de_palavras = abrir_arquivo()
                    continue
                if escolha == "1":
                    os.system("cls||clear")
                    break
                
            palavra_secreta = random.choice(lista_de_palavras)
            palavra_formatada = len(palavra_secreta) * '*'
            letras_acertadas = ''
            letras_tentadas = set()
            tentativas = len(set(palavra_secreta)) + len(set(palavra_secreta)) // 2

            # Inicio jogo
            while tentativas > 0:
                printar_estatisticas(letras_tentadas, tentativas, palavra_formatada)
            
                tentativa = input().lower()
                
                if len(tentativa) > 1:
                    os.system("cls||clear")
                    print("Digite apenas uma letra")
                    continue
                
                os.system("cls||clear") 
                if tentativa in palavra_secreta:
                    letras_acertadas += tentativa   
                    palavra_formatada = re.sub(f'[^{letras_acertadas}]', "*", palavra_secreta)
                    print(f"Letra acertada: {tentativa}")  
                else:
                    letras_tentadas.add(tentativa)
                    print(f"Letra incorreta: {tentativa}")
                    tentativas -= 1
                
                if palavra_formatada == palavra_secreta:
                    os.system("cls||clear")
                    print("Você venceu!!")
                    break
            else:
                os.system("cls||clear")
                print("Você perdeu :C")
                
            print(f"A palavra era {palavra_secreta}")
            
            jogar_dnv = input("Deseja jogar denovo? (s/n): ").lower()
            
            if jogar_dnv == "s":
                continue
            else:
                break
        
if __name__ == "__main__":
    main()