#Analise de dados
print('-' * 70)
sidade = 0
midade = 0
midadeh = 0
nomev = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'--- {p}ª pessoa ---')
    nome = str(input('nome: ')).strip()
    idade = int(input('Qual é a sua idade: '))
    sexo = str(input('Qual é seu sexo [M/F]: '))
    sidade += idade
    if p == 1 and sexo in 'Mm':
        midadeh = idade
        nomev = nome
    if sexo in 'Mm' and idade > midadeh:
        midadeh = idade
        nomev = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
midade = sidade / 4
print('-' * 70)
print(f'A média de idade do grupo é de {midade} anos.')
print(f'O homem mais velho tem {midadeh} anos e se chama {nomev}')
print(f'Ao total são {totmulher20} mulheres com menos de 20 anos.')
print('-' * 70)