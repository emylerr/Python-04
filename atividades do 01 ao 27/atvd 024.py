#jogo do ímpar ou par
from random import randint
from time import sleep

print('-' * 70)
print('JOGO DO ÍMPAR / PAR')

v = 0
while True:
    jog = int(input('Jogue seu número: '))
    comp = randint(0, 11)
    tot = jog + comp
    tip = ' '
    while tip not in 'PI':
        tip = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
        print('-' * 70)
        sleep(1.5)
    print(f'Você jogou {jog} e o computador {comp} no total de {tot}', end='')
    print(', Deu par' if tot % 2 == 0 else ', Deu ímpar')
    if tip == 'P':
        if tot % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tip == 'I':
        if tot % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
    sleep(1.5)
    print('-' * 70)
print(f'Você venceu {v} vezes.')
print('-' * 70)