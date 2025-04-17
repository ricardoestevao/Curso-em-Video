from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
maioridade = 18
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, date.today().year))
    print('Ainda faltam {} anos para o alistamento'.format(maioridade-idade))
    print('Seu alistamento será em {}'.format(date.today().year + saldo))
else:
    print('Seu alistamento foi em {}'.format(ano + maioridade))
