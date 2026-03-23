#Fatorial de um número com biblioteca.
from math import factorial
print('-' * 70)
n = int(input('Informe um valor para saber seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

#Em modo while
print('-' * 70)
n = int(input('Informe um número para saber seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
print('-' * 70)