import time, os

op = [
    (">", "<"),
    (">", ">"),
    ("<", ">"),
    ("<", "<") 
]

a = [0] * 11

for i in range(11):
    a[i] = [0] * 11

i_op = 0
while True:
    for i in range(11):
        for j in range(11):
            if eval(f"j {op[i_op][0]}= i and j{op[i_op][1]}= (10 - i)"):
                a[i][j] = 1

    i_op += 1
    if i_op > 3:
        i_op = 0
    
    os.system("cls")
    print(*a, sep="\n")
    for i in range(11):
        a[i] = [0] * 11
    time.sleep(1)
