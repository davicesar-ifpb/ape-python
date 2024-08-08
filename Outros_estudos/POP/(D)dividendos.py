n = int(input())

numero = input()

alice = ''
buba = ''

for idx,i in enumerate(numero):
    if (idx+1) % 2 == 0:
        alice += str(i)
        buba += "0"
    else:
        buba += str(i)
        alice += "0"
        
print(alice)
print(buba)