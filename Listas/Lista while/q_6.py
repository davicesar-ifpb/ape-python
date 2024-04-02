chico = 1.50
ze = 1.10

chico_taxa = 0.02
ze_taxa = 0.03


anos = 0
while chico < ze:
    chico += chico_taxa
    ze += ze_taxa
    anos += 1
print(anos)

