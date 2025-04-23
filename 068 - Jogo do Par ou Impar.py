# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from colorama import Fore, Back, Style, init
from random import randint

# Inicializa o colorama para funcionar corretamente no Windows
init()

print(Fore.YELLOW + Back.GREEN + '=-' * 20 + Style.RESET_ALL)
print(Fore.BLUE + 'VAMOS JOGAR PAR OU IMPAR' + Style.RESET_ALL)
print(Fore.YELLOW + Back.GREEN + '=-' * 20 + Style.RESET_ALL)
print('=-'*30)
computador = randint(1, 11)
valor = int(input('Diga um valor: '))
total = valor + computador
opcao = str(input('Par ou Impar? [P/I] ')).upper().split()[0]
print('=-'*20)
print(f'Você jogou {valor} e o computador jogou {computador}. Total de {total}')
if total % 2 == 0:
    print('PAR')
else:
    print('IMPAR')

print('=-'*20)