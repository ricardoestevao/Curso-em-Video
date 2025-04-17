n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

valores = [n1, n2, n3] # Cria uma lista
menor = min(valores) # Identifica o menor (min) valor da lista
maior = max(valores) # Identifica o maior (max) valor da lista

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

