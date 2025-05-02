# num = [2, 5, 9, 1]
# num[2] = 3  # Substituindo o terceiro item da lista (9) por (3)
# num.append(10)  # Acrescentando o número 10 à lista
# num.sort()  # Irá deixar os números em ordem crescente
# num.sort(reverse=True)  # Irá deixar os números em ordem decrescente
# num.insert(2, 0) # Irá acrescentar na casa 2 o número 0
# num.pop(2) # Irá remoover o elemento 2 da lista
# num.remove(2) # Irá remover o elemento x da lista (Ex. Elemento 2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: '))) # Irá criar uma lista de valores através do valor de entrada que o usuario digitar. 

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!') # Esse "end = ' '" é manter o código na mesma linha. 
# print('Cheguei ao final do programa')

# a = [2, 3, 4, 7]
# b = a[:] # Irá criar uma cópiada lista A
# b[2] = 8 # Estou alterando a posição 2 para o valor 8
# print(f'lista A:{a}')
# print(f'lista B: {b}')

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
mai = 0
men = 0
for c in range (0, 5):
    valores.append(int(input(f'DIGITE UM VALOR PARA A POSIÇÃO: {c}:')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
            if valores[c] < men:
                men = valores[c]
print('=-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai}')
print(f'O menor valor digito foi {men}')