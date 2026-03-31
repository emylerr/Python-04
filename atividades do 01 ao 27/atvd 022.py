#teste / braek
print('-' * 70)
print('NÚMEROS E SUA SOMA')
c = 0
s = 0
while True:
    n = int(input('Me fale um número até 999: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} números e a soma é de: {s}.')
print('-' * 70)