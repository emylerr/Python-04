#Progressão aritmética
ter = int(input('Digite o primeiro termo: '))
raz = int(input('Qual é a razão: '))

print('-' * 70)
dec = ter + (10-1) * raz
for c in range(ter, dec + raz, raz):
    print(f'{c}', end='⭢ ')
print('Final.')
print('-' * 70)