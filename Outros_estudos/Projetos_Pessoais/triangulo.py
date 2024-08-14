def triangulo(base: int, inverso: bool) -> None:
    ponta = 0 if base % 2 == 0 else 1
    indices = range(ponta, base + 1, 2)
    
    if inverso:
        indices = reversed(indices)
    
    for i in indices:
        print(f"{'*' * i: ^{base}}")


triangulo(base=5, inverso=0)
