# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0): # parâmetros com valores padrão
    """
    Mostra a ficha de um jogador.
    :param nome: nome do jogador (opcional)
    :param gols: número de gols marcados (opcional)
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.') #f-strings para formatação de strings

# Programa Principal
n = str(input('Nome do jogador: ')).strip() # remove espaços em branco no início e no fim
g = input('Número de gols: ') # input para receber dados do usuário

if g.isnumeric(): # verifica se a entrada é numérica
    g = int(g) # converte para inteiro
else: # se não for numérico, define gols como 0
    g = 0 # define gols como 0

if n == '': # se o nome estiver vazio, define como '<desconhecido>'
    ficha(gols=g) # chama a função ficha com gols como parâmetro
else: # se o nome não estiver vazio, chama a função ficha com nome e gols
    ficha(n, g) # chama a função ficha com nome e gols

