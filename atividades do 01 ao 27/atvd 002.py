#contagem regressiva de 10 até 0 com 1s de pausa entre eles.
from time import sleep

print('-' * 70)
print('OS FOGOS VÃO COMEÇAR!!')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOOW!')
print('FELIZ ANO NOVO!')
print('-' * 70)