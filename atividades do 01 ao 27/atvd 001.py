#Teoria / teste
print('-' * 70)
num = int(input('Digite um número: '))
for c in range(0, num+1):
    print(c)
print('Final da execução.')
print('-' * 70)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('Final da execução!')
print('-' * 70)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
print('-' * 70)