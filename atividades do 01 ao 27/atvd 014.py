#sexo M ou F
print('-' * 70)
sexo = str(input('Informe sua sexualidade [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Sexualidade\033[31m inválida \033[m, insira novamente: ')).strip().upper()[0]
print(f'Sexo {sexo}\033[32m válido \033[m, obrigada!')
print('-' * 70)