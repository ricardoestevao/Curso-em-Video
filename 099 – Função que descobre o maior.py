#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior (* núm): # função que recebe vários parâmetros
    cont = maior = 0 # cont = contador, maior = maior valor
    print('\nAnalisando os valores passados..')
    for valores in núm: # para cada valor em núm
        print(f'{valores} ', end='', flush=True) # imprime o valor sem pular linha
        sleep(0.3) # pausa de 0.3 segundos para melhor visualização
        if cont == 0: # se for 0 o primeiro valor
            maior = valores # o maior valor é o primeiro
        else: # se não for o primeiro valor
            if valores > maior: # se o valor for maior que o maior valor
                maior = valores # o maior valor é o valor atual
        cont += 1 # incrementa o contador
    print(f'Foram informados {cont} valores ao todo')            
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(10, 6, 4, 8, 7, 5)
maior(64, 56)
maior(321, 654)
maior(5)
maior()