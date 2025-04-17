import random # Função de sorteio

a = str(input('Primeiro Aluno: '))
b = str(input('Segundo Aluno:'))
c = str(input('Terceiro Aluno: '))
d = str(input('Quarto Aluno: '))

lista = [a, b, c, d]

print('O aluno escolhido foi {}'.format(random.choice(lista)))