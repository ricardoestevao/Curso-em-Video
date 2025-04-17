largura = float(input('Qual a largura da parede? '))
AP = float(input('Qual a altura da parede? '))
print('Sua parede tem a dimensão de {} x {} e sua área é de {}'.format(largura, AP, largura*AP))
print('Para pintar essa parede, você precisará de {:.2f} l de tinta.'.format((largura*AP)/2))