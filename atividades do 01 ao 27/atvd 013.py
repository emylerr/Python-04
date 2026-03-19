#while / teste
#conta até 10
print('-' * 70)
c = 1
while c < 11:
    print(c)
    c += 1
print('Final')

#Pergunta infinitamente até digitar 0
print('-' * 70)
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Final')

#Pergunta um valor e se quer continuar
print('-' * 70)
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]? ')).upper()
print('Final')

#Conta quantos números ímpares e pares
print('-' * 70)
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')
print('-' * 70)