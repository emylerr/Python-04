#Soma dos pares.
s = 0
cont = 0
print('-' * 70)
for c in range(1, 7):
    n = float(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} números pares, e a soma é de: {s}.')
print('-' * 70)