#24h - 86400 s
# 1 = 3600 s
descricao, dia = input().split()
dia = int(dia)
hora, minuto, segundo = [int(x) for x in input().split(" : ")]
descricao2, dia2 = input().split()
dia2 = int(dia2)
hora2, minuto2, segundo2 = [int(x) for x in input().split(" : ")]

dia_em_s1, dia_em_s2 = (dia * 86400), (dia2 * 86400)
hora_em_s1,hora_em_s2 = (hora * 3600), (hora2 * 3600)

total1,total2 = (dia_em_s1 + hora_em_s1 + segundo), (dia_em_s2 + hora_em_s2 + segundo2)

diferenca = (total2 - total1)
dia_final = diferenca // 86400
resto_dia = diferenca % 86400
hora_final = resto_dia // 3600
resto_hora = resto_dia % 3600
minuto_final = resto_hora // 60
resto_minuto = resto_hora % 60
segundo = resto_minuto

print(f"{dia_final} dia(s)")
print(f"{hora_final} hora(s)")
print(f"{minuto_final} minuto(s)")
print(f"{segundo} segundo(s)")