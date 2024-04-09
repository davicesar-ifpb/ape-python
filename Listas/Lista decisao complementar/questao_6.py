""" Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
nota maior ou igual a 8.0 para ser aprovado no concurso.
Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
foi aprovado ou não no concurso. """


def checar_aprovado(media):
    if media < 7:
        return print("Candidato reprovadado na primeira etapa")
    
    nota_segunda_etapa = int(input("Nota da prova da segunda etapa: "))
    
    if nota_segunda_etapa < 8:
        return print("Candidato reprovado na segunda etapa")
    
    return print("Cadidato aprovado no concurso")

def main():
    nota_1 = int(input("Nota 1 da primeira etapa: "))
    nota_2 = int(input("Nota 2 da primeira etapa: "))

    media_primeira_etapa = (nota_1 + nota_2) / 2

    checar_aprovado(media_primeira_etapa)

if __name__ == "__main__":
    main()
    


        
# if media_primeira_etapa >= 7:
#     nota_segunda_etapa = int(input("Nota da prova da segunda etapa: "))
#     if nota_segunda_etapa >= 8:
#         print("Candidato aprovado no concurso")
#     else:
#         print("Candidato reprovado na segunda etapa")
# else:
#     print("Canditado reprovado na primeira etapa.")