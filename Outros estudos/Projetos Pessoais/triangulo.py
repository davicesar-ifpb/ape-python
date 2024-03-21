def triangulo(base:int,inverso:bool) -> print:
    j = base
    if inverso == False:
        j = 2 if base % 2 == 0 else 1
        for _ in range(base):
            print(f"{'*' * j: ^{base}}")
            j += 2
            if j > base:
                break
    else:
        for _ in range(base):
            print(f"{'*' * j: ^{base}}")
            j -= 2
            if j <= 0:
                break


triangulo(11,False)