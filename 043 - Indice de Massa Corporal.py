peso = float(input('Qual é o seu peso? (KG)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('O IMC dessa pessoa é de {:.1f}, você está abaixo do peso'.format(imc))
elif imc <= 25:
    print('O IMC dessa pessoa é de {:.1f}, você está no peso ideal'.format(imc))
elif imc <= 30:
    print('O IMC dessa pessoa é de {:.1f}, você está com sobrepeso'.format(imc))
elif imc <= 40:
    print('O IMC dessa pessoa é de {:.1f}, você está com obesidade'.format(imc))
elif imc > 40:
    print('O IMC dessa pessoa é de {:.1f}, você está com obesidade mórbida'.format(imc))
