from random  import randint # Importando a função randint do módulo random
from time import sleep # Importando a função sleep do módulo time
from operator import itemgetter # Importando a função itemgetter do módulo operator
# Criando um jogo de dados onde 4 jogadores jogam e o programa sorteia um valor de 1 a 6 para cada jogador.
jogo = {'jogador1': randint(1, 6), #{# Criando um dicionário com os jogadores e seus respectivos valores}
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict() # Criando um dicionário vazio para o ranking
print('Valores sorteados:') # Imprimindo os valores sorteados
for k, v in jogo.items ():
    print(f'{k} tirou {v} no dado.') # Imprimindo o nome do jogador e o valor sorteado
    sleep(1) # Aguardando 1 segundo
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Ordenando o dicionário jogo pelo valor sorteado em ordem decrescente
print('Ranking dos jogadores:') # Imprimindo o ranking dos jogadores
for i, v in enumerate(ranking): # Enumerando o ranking
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}') # Imprimindo a posição do jogador, o nome e o valor sorteado
    sleep(1) # Aguardando 1 segundo
    