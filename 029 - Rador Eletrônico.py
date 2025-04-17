velocidade = float(input('Qual é a velocidade atual do carro em KM/h? '))
multa = (velocidade-80)*7

if velocidade < 80:
    print('\033[1:33mTenha um bom dia! Dirija com segurança!')
else:
    velocidade > 80
    print('\033[1:31mVocê foi multado! Excedeu o limite de velocidade de 80 km/h e receberá uma multa de R$ {:.2f}'.format(multa))
