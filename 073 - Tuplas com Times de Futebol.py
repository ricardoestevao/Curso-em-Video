# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Palmeiras', 'Bragantino', 'Cruzeiro'
         'Fluminense', 'Internacional', 'Bahia', 'Botafogo'
         'Ceará SC', 'São Paulo', 'Vasco da Gama', 'Corinthians'
         'Juventude', 'Mirassol', 'Fortaleza', 'EC Vitória',
         'Atlético-MG', 'Grêmio', 'Santos', 'Sport Recife')
print('--=' * 30)
print(f'Lista de times: {times}')
print('--=' * 30)

# a) Os 5 primeiros times.

print(f'Os 5 primeiros times são {times[0:5]}')
print('--=' * 30)

# b) Os últimos 4 colocados.

print(f'Os ultimos 4 times colocado são {times[-4:]}')
print('--=' * 30)

# c) Times em ordem alfabética.

print(f'Times em ordem alfábética: {sorted(times)}') # 'Sorted é um comando para ordenar a tupla ou seja deixar em ordem alfabética
print('--=' * 30)

# d) Em que posição está o time da São Paulo.

print(f'O São Paulo está na {times.index('São Paulo')+1}° posição.')