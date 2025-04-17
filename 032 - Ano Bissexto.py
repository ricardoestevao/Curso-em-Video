from datetime import date #Modulo para saber o ano atual
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Código para sabermos o ano atual caso o usuário digite '0'.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O {} é BISSEXTO'.format(ano))
else:
    print('O {} NÃO é BISSEXTO'.format(ano))