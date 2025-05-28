# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
from time import sleep

def contador(i, f, p): # i = início, f = fim, p = passo
    print(f'Contagem de {i} até {f} de {p} em {p}') # cabeçalho da função
    sleep(2) # pausa de 2 segundos para melhor visualização
    if p < 0: # se o passo for negativo
        p*= -1 # transforma o passo em positivo
    if p == 0: # se o passo for igual a zero
        p = 1 # transforma o passo em 1 para evitar loop infinito    
    if i < f:   # se o início for menor que o fim
        cont = i # variável contadora inicia com o valor de i
        while cont <= f: # enquanto cont for menor ou igual a f
            print(f'{cont} ', end= '', flush=True) # imprime o valor de cont sem pular linha
            sleep(0.5)  # pausa de 0.5 segundos para melhor visualização
            cont = cont + p # incrementa cont pelo valor de p
        print('FIM!')
    else: # se o início for maior que o fim
        cont = i # variável contadora inicia com o valor de i
        while cont >= f: # enquanto cont for maior ou igual a f
            print(f'{cont} ', end='', flush=True) # imprime o valor de cont sem pular linha
            sleep(0.5)
            cont = cont - p # decrementa cont pelo valor de p
        print('FIM!')        
# Programa principal
contador(0, 10, 1) 
contador(10, 0, 1)
print('Agora é sua vezde personalizar a contagem!')
ini = int(input('Início: ')) # solicita o início da contagem
fim = int(input('Fim:    ')) # solicita o fim da contagem
pas = int(input('Passo:  ')) # solicita o passo da contagem
contador(ini, fim, pas) # chama a função contador com os valores informados pelo usuário