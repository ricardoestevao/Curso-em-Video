# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=-' * 15)
print('               JOGA NA MEGA SENA               ')
print('-=-' * 15)
quant = int(input('Quantos jogos vocÊ quer que eu sorteie? '))
tot = 1 # Para considerar a contagem a partir de 1 ao invés de 0.
while tot <= quant: # quantidade de jogos que o usúario soliciou 
    cont = 0
    while True:
      num = randint(1, 60)
      if num not in lista: # Se o número não estiver na lista será adicionado
            lista.append(num)
            cont += 1 # O contator irar passar para o próximo index (Ex: Adicionou o primeiro número, irar adicionar o 2° número)
      if cont >= 6: # Sorteando 6 números
            break
    lista.sort()
    jogos.append(lista[:]) # Criando uma cópia da lista principal
    lista.clear() # Apagando a lista
    tot += 1
print('-=-' * 3, f'SORTEANDO {quant} JOGOS', '-=-' * 3)
for i, l in enumerate(jogos): # Irar tratar o índice e a lista
     print(f'Jogo {i+1}: {l}')
     sleep(1) # Tempo de ação para resposta dos resultados. 
print('-=-' * 5, '< BOA SORTE! >', '-=-' * 5)