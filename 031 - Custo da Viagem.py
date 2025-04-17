distancia = float(input('Qual a distância da sua viagem? '))
if distancia < 200:
    print('O valor da sua passagem será de R$ {:.2f}'.format(distancia*0.50))
else:
    print('O valor da sua passagem será de R$ {:.2f}'.format((distancia*0.45)))