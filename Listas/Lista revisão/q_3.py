VALOR_PARA_CUPOM = 30


def distribuir_cupons(valor: float):
    qtd_cupons = int(valor // VALOR_PARA_CUPOM)
    saldo = valor % VALOR_PARA_CUPOM
    para_novo_cupom = VALOR_PARA_CUPOM - saldo

    return qtd_cupons, saldo, para_novo_cupom


def main():
    total_vendido = 0
    total_cupons = 0
    maior_valor_vendido = 0

    for _ in range(200):
        valor_compra = float(input())
        
        qtd_cupons, saldo, para_novo_cupom = distribuir_cupons(valor_compra)

        total_vendido += valor_compra
        total_cupons += qtd_cupons
        maior_valor_vendido = valor_compra if valor_compra > maior_valor_vendido else maior_valor_vendido

        if qtd_cupons == 0:
            print("Sem cupons")
        else:
            print(f"{qtd_cupons = }")

        print(f"{saldo = }")
        print(f"{para_novo_cupom} para novo cupom")
    
    print(f"{total_vendido = }")
    print(f"{total_cupons = }")
    print(f"Maior valor vendido: {maior_valor_vendido} \
        | {maior_valor_vendido // 30}")

if __name__ == "__main__":
    main()