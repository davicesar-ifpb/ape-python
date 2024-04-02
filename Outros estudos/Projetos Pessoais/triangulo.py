def triangulo(base:int,inverso:bool) -> print:
    j = base
    if inverso:
        for _ in range(base):
            print(f"{'*' * j: ^{base}}")
            j -= 2
            if j <= 0:
                break
        
    else:
        j = 2 if base % 2 == 0 else 1
        for _ in range(base):
            print(f"{'*' * j: ^{base}}")
            j += 2
            if j > base:
                break
        

triangulo(base=31,inverso=True)