#números primeos
print('-' * 70)
n = int(input('Digite um número: '))

tot = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[35m', end='')
    print(f'{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {tot} vezes.')
print('-' * 70)
if tot == 2:
    print('O número é primo!')
else:
    print('O número não é primo.')
print('-' * 70)