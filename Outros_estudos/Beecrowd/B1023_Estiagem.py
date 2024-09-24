import sys

cidade = 1
while True:
    
    n = int(input())
    if n == 0:
        break
    
    if cidade > 1:
        sys.stdout.write('\n')
    
    consumos = {}
    consumo_total = 0
    total_moradores = 0
    for i in range(n):
        qtd_moradores, consumo_imovel = map(int, sys.stdin.readline().split())
        consumo_total += consumo_imovel
        total_moradores += qtd_moradores
        consumos[consumo_imovel//qtd_moradores] = consumos.get(consumo_imovel//qtd_moradores, 0) + qtd_moradores
    
    sys.stdout.write(f'Cidade# {cidade}:\n')
    sys.stdout.write(' '.join(f'{qtd_moradores}-{consumo}' for consumo, qtd_moradores in sorted(consumos.items())))
    sys.stdout.write('\n')

    consumo_medio = consumo_total / total_moradores
    truncado = float(str(consumo_medio)[:str(consumo_medio).find('.') + 3])
    sys.stdout.write(f"Consumo medio: {truncado:.2f} m3.\n")
        
    cidade += 1