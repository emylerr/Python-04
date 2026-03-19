#Melhoria do jogo
'''import random
from time import sleep
n = int(input('Qual foi o número que o computador pensou? '))
num = random.randint(0, 5)
print('Pensando...')
sleep(2)
print(f'O número escolhido foi {num}.')

if n == num:
    print('Parabéns, você venceu!')
else:
    print('Tente novamente!')'''

from random import randint
print('-' * 70)
comp = randint(0, 10)
print('Já pensei em um número entre 0 e 10, será que você adivinhou?')

acert = False
palp = 0
while not acert:
    jog = int(input('Qual é seu palpite? '))
    palp += 1
    if jog == comp:
        acert = True
        print('-' * 70)
    elif jog > comp:
        print('Um pouco menos, jogue de novo.')
    else:
        if jog < comp:
            print('Um pouco mais, jogue de novo.')
print(f'Você acertou com {palp} tentativas!')
print('-' * 70)