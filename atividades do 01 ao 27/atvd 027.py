#caixa eletronico
from time import sleep
print('-' * 70)
print('{:^70}'.format(' CAIXA ELETRÔNICO '))
print('-' * 70)

val = int(input('Digite qual valor você quer sacar? R$'))
tot = val
ced = 50
totc = 0

while True:
    if tot >= ced:
        tot -= ced
        totc += 1
    else:
        if totc > 0:
          sleep(1.2)
          print(f'{totc} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totc = 0
        if tot == 0:
            break
print('Volte sempre ao banco!')
print('-' * 70)