#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = 0
atual = date.today().year
idade = atual - ano
totmaior = 0
totmenor = 0

for c in range (1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))