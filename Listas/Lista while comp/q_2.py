def primos(quantidade):
    j = 1    
    while j <= quantidade:
        for i in range(1,j+1):
            if j == 1:
                print(f"{j} Não é primo")
                break
            
            if (j % i == 0) and j == i:
                print(f"{j} É primo")
                break
            elif (j % i == 0) and i < j and i != 1:
                print(f"{j} Não é primo")
                break
        j += 1
        
primos(50)