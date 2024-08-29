def onda(s, idx=0):
    if idx == len(s):
        return

    temp1 = s[:idx].lower()
    n = s[idx].upper()
    temp2 = s[idx+1:].lower()

    out = temp1 + n + temp2
    print(out)
    
    onda(out, idx + 1)

onda("eusouumaonda")