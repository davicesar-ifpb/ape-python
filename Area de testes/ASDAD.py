lista = [4,124,5,1,32,1]

print(4,124,5,1,32,1)

for  i in lista:
    print(i,end=" ")
print()

print("".join((str(lista)).split(",")).strip("[]"))

