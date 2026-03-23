#Vários valores.
print('-' * 70)
num = cont = soma = 0
num = int(input('Digite um número [999 para parar.]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar.]: '))
print(f'Você digitou {num} números e a soma entre eles é de: {soma}.')
print('-' * 70)