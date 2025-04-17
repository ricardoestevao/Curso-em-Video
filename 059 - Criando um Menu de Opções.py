# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
while True:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('[1] SOMAR' \
          '\n[2] MULTIPLICAR' \
          '\n[3] MAIOR' \
          '\n[4] NOVOS NÚMEROS' \
          '\n[5] SAIR DO PROGRAMA')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'O produto de {n1} e {n2} é {n1 * n2}')
    elif opcao == 3:
        maior = max(n1, n2)  # Identifica o maior número
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe os números novamente.')
        continue
    elif opcao == 5:
        print('Finalizando o programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    print('-' * 30)
