import time, os

op = [
    (">", "<"),
    (">", ">"),
    ("<", ">"),
    ("<", "<") 
]

matriz = [0] * 11

for i in range(11):
    matriz[i] = [0] * 11

i_op = 0
while True:
    for i in range(11):
        for j in range(11):
            if eval(f"j {op[i_op][0]}= i and j{op[i_op][1]}= (10 - i)"):
                matriz[i][j] = 1
                continue
            
            matriz[i][j] = 0
    
    i_op += 1
    if i_op > 3:
        i_op = 0
    
    os.system("cls")
    print(*matriz, sep="\n")
    time.sleep(1)
