casos = int(input())

for _ in range(casos):
    
    a,b,c,L,R = map(int, input().split())
    
    ponto_possivel = 0
    for i in range(L,R+1):
        y = ((a/b)*i) + c
        
        if y == int(y):
            ponto_possivel += 1
            
    print(ponto_possivel)
        
