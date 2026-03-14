#números pares
from time import sleep

print('-' * 70)
print('Números pares entre 1 e 50 são:')

for c in range(2, 51, 2):
    print(c)
    sleep(0.5)
print('Fim da exibição dos números pares.')
print('-' * 70)