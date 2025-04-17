d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM  ele rodou?'))
td = d * 60
tkm = km * 0.15
print('O total a ser pagar é R$ {}'.format(td+tkm))