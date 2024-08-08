ALFABETO = "abcdefghijklmnopqrstuvxz"
VOGAIS = ["a", "e", "i", "o", "u"]
CONSOANTES = "bcdfghjklmnpqrstvxz"

entrada = input()

palavra_criptograda = ""

for i in entrada:
    
    if i == "z":
        palavra_criptograda += "zuz"
    
    elif i in VOGAIS:
        palavra_criptograda += i
    
    else:
        palavra_criptograda += i
        
        consoante_insolada = VOGAIS.copy()
        consoante_insolada.append(i)
        consoante_insolada.sort()
        index = consoante_insolada.index(i)
        vogal_antes = consoante_insolada[index - 1]
        vogal_depois = consoante_insolada[index + 1]
        vogal_antes_index = ALFABETO.index(vogal_antes)
        vogal_depois_index = ALFABETO.index(vogal_depois)
        index_i_no_alfabeto = ALFABETO.index(i)
        
        if (vogal_depois_index - index_i_no_alfabeto) < (index_i_no_alfabeto - vogal_antes_index):
            palavra_criptograda += vogal_depois
        else:
            palavra_criptograda += vogal_antes
        
        index_i_nas_consoantes = CONSOANTES.index(i)
        palavra_criptograda += CONSOANTES[index_i_nas_consoantes+1]
            
print(palavra_criptograda)