#nome e preço
print('{:-^70}'.format(' LOJA RIBEIRO '))

totc = 0
totm = 0
m = 0
c = 0
bar = ''
while True: 
    prod = str(input('Nome do produto adquirido: '))
    val = float(input('Qual é o valor? R$'))
    c += 1
    totc += val
    if val > 1000:
        totm += 1
    if c == 1 or val < m:
        m = val
        bar = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar cadastrando outros itens? [S/N]: ')).strip().upper()[0]
        print('-' * 70)
    if resp == 'N':
        break
print(f'O total da compra foi de R${totc:.2f}.')
print(f'Existem {totm} produtos que custa mais de R$1000.00')
print(f'O produto mais barato foi {bar} e custa {m:.2f}')
print('{:-^70}'.format(' OBRIGADA POR COMPRAR CONOSCO! '))