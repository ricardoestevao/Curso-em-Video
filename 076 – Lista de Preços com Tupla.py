# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 2.75,
           'Caneta', 4.00,
           'Estoujo', 7.50,
           'Mochila', 90.50,
           'Tesoura', 10.00,
           'Livro', 150.00,
           'Compasso', 15.00,
           'Borracha', 4.00,
           'Caderno', 87.00)

print ('-' * 40) 
print(f'{"LISTAGEM DE PREÇOS":^40}') # Foi colocado essa formatação (^ = Centralizado) 40 caractares. 
print ('-' * 40) 
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')