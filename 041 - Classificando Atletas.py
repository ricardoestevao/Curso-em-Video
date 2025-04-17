from datetime import datetime
atual = datetime.today().year
nascimento = int(input('Qual o ano de Nascimento do(a) atleta: '))
idade = atual - nascimento
if idade <= 9:
    print('O(a) atleta que nasceu em {} tem {} anos e está na categoria MIRIM'.format(nascimento,idade ))
elif idade <= 14:
    print('O(a) atleta que nasceu em {} tem {} anos e está na categoria INFANTIL'.format(nascimento, idade))
elif idade <= 19:
    print('O(a) atleta que nasceu em {} tem {} anos e está na categoria JUNIOR'.format(nascimento, idade))
elif idade <= 25:
    print('O(a) atleta que nasceu em {} tem {} anos e está na categoria SÊNIOR'.format(nascimento, idade))
else:
    idade > 25
    print('O(a) atleta que nasceu em {} tem {} anos e está na categoria MASTER'.format(nascimento, idade))



