VALOR_PARA_CUPOM = 30


def distribuir_cupons(valor: float):
    qtd_cupons = int(valor // VALOR_PARA_CUPOM)
    saldo = valor % VALOR_PARA_CUPOM

    return qtd_cupons, saldo

def main():
    valor_compra = float(input())
    qtd_cupons, saldo = distribuir_cupons(valor_compra)
    
    if qtd_cupons == 0:
        print("Sem cupons")
    else:
        print(f"{qtd_cupons = }")

    
    print(f"{saldo = }")
    print(f"{VALOR_PARA_CUPOM - saldo} para novo cupom")

if __name__ == "__main__":
    main()