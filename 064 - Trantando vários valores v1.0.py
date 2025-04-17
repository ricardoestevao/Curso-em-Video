# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n1 = cont = 0

n1 = int(input('Digite um número [999 para parar]: '))
while n1 != 999:
        n1 = int(input('Digite um número [999 para parar]: '))
        cont += 1
print(f'Você digitou {cont} números e soma deles deu {n1 - 999}.')   
