# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

números = list()
pares = list()
impares = list()

while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r in 'nN':
        break

for i, v in enumerate(números):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print('-=-' * 30)
print(f'A lista completa é {números}')
print(f'A lista em pares são {pares}')
print(f'A lista em impáres são {impares}')