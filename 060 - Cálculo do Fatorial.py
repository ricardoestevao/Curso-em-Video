# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
n1 = int(input('Digite um número para calular seu Fatorial: '))
f = factorial(n1)
print(f'O fatorial de {n1} é {f}')
