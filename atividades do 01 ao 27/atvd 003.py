#números pares
from time import sleep

print('Números pares entre 1 e 50 são:')
print('-' * 70)

for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.5)
print('Final.')