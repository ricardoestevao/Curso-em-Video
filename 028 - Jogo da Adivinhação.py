import random
from time import sleep # Importador da biblioteca a função (TEMPO) sleep para esperar 'X' segundos para prosseguir para o próximo código

numero = random.randint(1, 2) # Faz o computador "PENSAR"
print('\033[0:33m -=-'*30)
print('\033[0:31M Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[0:33m -=-'*30)
jogador = int(input('Em que número em pensei ?')) # Jogador tenta adivinhar
print('\033[1:36m PROCESSANDO....')
sleep(2)

if jogador == numero:
    print('Você acertou, PARABÉNS!')
else:
    print('Tente novamente! Eu pensei no número {} e não no número {}'.format(numero, jogador))

