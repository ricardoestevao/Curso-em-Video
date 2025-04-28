#Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. 
#As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim','Bata Frita')

# Duas maneiras de representar o 'for'

# for cont in range(0, len(lanche)): 
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}') # Código irar informar além do nome do item vai exibir a posição dele dentro da tuplas

# for comida in lanche: # Esse tipo de código não informa a posição do item na tupla. 
#     print(f'Eu vou comer {comida}')

# for pos, comida in enumerate (lanche): # Código irar informar além do nome do item vai exibir a posição dele dentro da tuplas
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!')

# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente! ', end='')
    print(f'Você digitou o número {cont[num]}')

    opcao = input('Quer continuar? [S/N] ').strip().upper()
    if opcao == 'N':
        print('Programa encerrado. Até a próxima!')
        break    
     