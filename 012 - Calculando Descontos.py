produto = float(input('Qual o preço do produto? '))
desconto = produto - (produto * 10 / 100)
print('O item que custava R$ {}, na promoção de 10% vai custar {}'.format(produto, desconto))
