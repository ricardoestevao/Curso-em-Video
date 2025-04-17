from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print((('''Escolha uma das opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')))
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogada]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print('O JOGADOR VENCE!')
    elif jogada == 2:
        print('O COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: # computador jogou PAPEL
    if jogada == 0:
        print('O COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print ('O JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')    

elif computador ==2: # computador jogou TESOURA
    if jogada == 0:
        print('O JOGADOR VENCE!')
    elif jogada == 1:
        print('O COMPUTADOR VENCE!')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')    