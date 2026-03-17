#Detector de palíndromo
print('-' * 70)
frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
junt = ''.join(pal)
inv = ''
print('-' * 70)

for let in range(len(junt) - 1, -1, -1):
    inv += junt[let]
print(f'O inverso de {junt} é {inv}')
if inv == junt:
    print(f'Sua frase é um palíndromo.')
else:
    print(f'A frase não é um palíndromo.')
print('-' * 70)