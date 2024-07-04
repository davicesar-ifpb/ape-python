VALOR_PARA_CUPOM = 30


def distribuir_cupons(valor: float) -> int:
    return int(valor // VALOR_PARA_CUPOM)


def main():
    valor_compra = float(input())
    qtd_cupons = distribuir_cupons(valor_compra)
    print(f"{qtd_cupons = }")

if __name__ == "__main__":
    main()