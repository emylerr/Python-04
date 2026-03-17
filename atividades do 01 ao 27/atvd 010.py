#Maioridade
from datetime import date
atual = date.today().year
print('-' * 70)

totma = 0
totme = 0
for pess in range(1, 8):
    ano = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        totma += 1
    else:
        totme += 1
print('-' * 70)
print(f'Ao todo tivemos {totma} pessoas maiores de idade.')
print(f'E também tivemos {totme} pessoas menores de idade.')
print('-' * 70)