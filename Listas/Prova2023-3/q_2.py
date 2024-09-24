def criptografa(mensagem):
    nova_mensagem = ""
    
    for i in mensagem:
        if i == "a" or i == "A":
            nova_mensagem += "@"
            
        elif i == "e" or i == "E":
            nova_mensagem += "3"
            
        elif i == "i" or i == "I":
            nova_mensagem += "!"
        
        else:
            nova_mensagem += i
            
    return nova_mensagem


# Testes
print(criptografa("Hello World!"))
print(criptografa("I love Python!"))
print(criptografa("Meu nome é Davi!"))