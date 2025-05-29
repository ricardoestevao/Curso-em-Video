# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(lista): # Função para sortear 5 valores de uma lista
    print('Sorteando 5 valores da lista: ', end= '') # Função para sortear 5 valores de uma lista
    for cont in range(0, 5): # Loop para sortear 5 valores
        n = randint(1, 10) # Sorteia um número aleatório entre 1 e 10
        lista.append(n) # Adiciona o número sorteado à lista
        print(f'{n} ', end='', flush=True) # Imprime o número sorteado
        sleep(0.3) # Atraso de 0.3 segundos para simular o sorteio
    print('PRONTO!') # Imprime a mensagem de que o sorteio foi concluído

def somapar(lista): # Função para somar os valores pares da lista
    soma = 0 # Variável para armazenar a soma dos valores pares
    for valor in lista: # Loop para percorrer os valores da lista
        if valor % 2 == 0: # Verifica se o valor é par
            soma += valor # Adiciona o valor par à soma
    print(f'Somando os valores pares de {lista} temos {soma}') # Imprime a soma dos valores pares da lista

# Programa Principal
números = list() # Lista para armazenar os números sorteados
sorteia(números) # Chama a função para sortear os números
somapar(números) # Chama a função para somar os valores pares da lista