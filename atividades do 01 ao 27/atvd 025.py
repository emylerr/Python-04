#análise de dados
print('-' * 70)
print('CADASTRO DE PESSOAS!')

toti = 0
toth = 0
totf = 0
while True:
    id = int(input('Digite a idade: '))
    sex = ' '
    while sex not in 'FM':
        sex = str(input('Qual é o sexo [F/M]? ')).strip().upper()[0]
    if id >= 18:
        toti += 1
    if sex == 'M':
        toth += 1
    if sex == "F" and id < 20:
        totf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 70)
    if resp == 'N':
        break
print(f'O total de pessoas que tem mais de 18 anos é: {toti}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totf} mulheres com menos de 20 anos.')
print('-' * 70)