# Crie um programa que vai ler vários números e colocar em uma lista.   
#  Depois disso, mostre:         
# A) Quantos números foram digitados.  
# B) A lista de valores, ordenada de forma decrescente.   
# C) Se o valor 5 foi digitado e está ou não na lista.

números = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        r = str(input('Deseja continuar? [S/N]').strip().upper())
        if r in 'nN':
            break
print ('-=-' * 30)
print(f'Você digitou {len(números)} elementos')
print(f'Os valores em ordem decrescente são {sorted(números, reverse=True)}') # Ordenação decrescente
if 5 in números:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na listagem')
