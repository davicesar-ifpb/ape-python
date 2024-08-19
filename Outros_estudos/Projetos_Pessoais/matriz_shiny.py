import os
import time

n = 9
m = [[0] * n for _ in range(n)]

while True:
    
    # Direção:  ↘️
    for k in range(n * 2):
        os.system('cls')
        for i in range(n):
            for j in range(n):
                if (i + j) == k:
                    m[i][j] = 1
                else:
                    m[i][j] = 0
                
                print(m[i][j], end=' ')
            print()
        time.sleep(0.1)
    
    
    # Direção:  ↙️
    for k in range(-n, n):
        os.system('cls')
        for i in range(n):
            for j in range(n):
                if (i - j) == k:
                    m[i][j] = 1
                else:
                    m[i][j] = 0  
                
                print(m[i][j], end=' ')
            print()
        time.sleep(0.1)
        
        
    # Direção:  ↖️
    for k in reversed(range(n * 2)):
        os.system('cls')
        for i in range(n):
            for j in range(n):
                if (i + j) == k:
                    m[i][j] = 1
                else:
                    m[i][j] = 0
                
                print(m[i][j], end=' ')
            print()
        time.sleep(0.1) 
        
        
    # Direção:  ↗️    
    for k in reversed(range(-n, n)):
        os.system('cls')
        for i in range(n):
            for j in range(n):
                if (i - j) == k:
                    m[i][j] = 1
                else:
                    m[i][j] = 0  
                
                print(m[i][j], end=' ')
            print()
        time.sleep(0.1)