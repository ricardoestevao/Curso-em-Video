# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

jogador = dict()
partidas = list()
jogador ['nome'] = str(input('Nome do jogador: ')) # Criando dentro do dicionário jogador a chave 'Nome' e solicitando ao usúario o nome do jogador. 
tot = int(input(f'Quantos partidas {jogador["nome"]} jogou?')) # Criando uma variável comum apenas para saber a quantidade de partidas. 
for c in range(0, tot): # Fazendo um contador de partidas e gols realizados em cada partida.
    partidas.append(int(input(f'Quantos gols na partida {c+1}?'))) # Será adiconado a lista 'partidas' a quantidade de gols feito
jogador['goals'] = partidas[:] # Criando uma chave 'GOALS' que irar receber uma cópia dos valores da lista 'partidas'
jogador['total'] = sum(partidas) # Criando uma nova chave 'TOTAL' que irar receber a somatória dos valores de goals nas partidas
print('-=-' * 30)
print(jogador)
print('-=-' * 30)
for k, v in jogador.items(): # Criando uma interação
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["goals"])} partidas') # Lendo o nome do jogador e quantas partidas o mesmo jogou.
for i,v in enumerate(jogador['goals']):
    print(f'          => Na partida {i}, fez {v} goals.')
print(f'Foi um total de {jogador["total"]} goals.')
