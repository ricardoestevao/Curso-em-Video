#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

# ...código existente...

total = produto_mil = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')  # Inicializa com infinito para garantir que qualquer preço será menor

while True: 
    produto = str(input('Nome do produto?: '))
    preco = float(input('Preço: R$ '))
    total += preco

    # Verifica se o preço do produto atual é menor que o preço mais barato registrado
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = produto

    if preco > 1000:
        produto_mil += 1

    opcao = ' '
    while opcao not in 'SN': 
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    
    if opcao == 'N':
        break

print('-' * 30)
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {produto_mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi "{produto_mais_barato}" que custa R$ {preco_mais_barato:.2f}')