def fibonacci(n):
    x = ( (((1 + (5**(1/2))) /2) **n) - (((1 - (5**(1/2))) /2) **n) ) / (5 ** (1/2))
    return x

print(f"{fibonacci(int(input())):.1f}")