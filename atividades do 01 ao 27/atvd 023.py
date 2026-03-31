#tabuada versão 3
from time import sleep
print('-' * 70)
while True:
    n = int(input('Você quer ver a tabuada de qual valor? '))
    sleep(1.2)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 70)
print('O programa foi encerrado, volte ao início.')
print('-' * 70)