#números ímpares e múltiplos de 3
from time import sleep

print('-' * 70)
print('Os números ímpares que são múltiplos  de 03 são: ')

s = 0
cont = 0
for c in range(3, 501, 6):
    print(c)
    sleep(0.1)
    s += c
    cont += 1
sleep(0.5)
print(f'Existem {cont} números') 
sleep(1)
print(f'E a soma deles é de: {s}')
print('-' * 70)