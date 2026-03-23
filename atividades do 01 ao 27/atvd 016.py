#tabela de valores
from time import sleep
print('-' * 70)
n1 = int (input('Informe o 1º valor: '))
n2 = int (input('Informe o 2º valor: '))

opcao = 0
while opcao != 5:
    print('''    [01] - Somar
    [02] - Multiplicar
    [03] - Maior
    [04] - Novos números
    [05] - Sair do programa''')
    opcao = int(input('Qual é a sua escolha? '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é de: {soma}')
        print('-' * 70)
    elif opcao == 2:
        produto = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é de: {produto}')
        print('-' * 70)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é: {maior}')
        print('-' * 70)
    elif opcao == 4:
        print(f'Informe os números novamente!')
        n1 = int(input('Informe o 1º número: '))
        n2 = int(input('Informe o 2º número: '))
        print('-' * 70)
    elif opcao == 5:
        print(f'Finalizando...')
        print('-' * 70)
    else:
        print('Opção inválida, volte no ínicio.')
    sleep(1)
print('Fim do programa, obrigada.')
