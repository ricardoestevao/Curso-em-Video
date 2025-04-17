#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = float('-inf') # Inicializa com o menor valor possível
menor = float('inf') # Inicializa com o maior valor possível

for c in range(5):
    peso = float(input(f'Digite o peso da {c + 1}ª pessoa: '))
    if peso > maior:
        maior = peso # Atualizada para o maior peso
    if   peso < menor:
        menor = peso # Atualiza o menor peso
print(f'O maior peso foi {maior} KG')
print(f'O menor peso foi {menor} KG')