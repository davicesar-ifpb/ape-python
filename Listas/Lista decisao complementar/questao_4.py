""" Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando
apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
O programa deve mostrar o resultado obtido. """


inicial = int(input("Hora inicial: "))
final = int(input("Hora final: "))


diferenca = final - inicial

if diferenca < 0:
    diferenca += 24
    
print(diferenca, "horas")