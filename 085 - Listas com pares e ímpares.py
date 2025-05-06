# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

temp = [] # Lista temporária para armazenar os números
princ = [[], []] # Lista principal com duas sublistas: [pares, ímpares]

for n in range (1, 8): # Itera de 1 a 7
    valor = int(input(f'Digite o {n}° valor: '))
    if valor % 2 == 0: # Verifica se o número é par
        princ[0].append(valor)
    else: # Caso contrário, é impar
        princ[1].append(valor)
    
#Ordena os valores pares e impares
princ[0].sort()
princ[1].sort()

#Exibe resultados
print(f'Os pares digitados foram: {princ[0]}')
print(f'Os impares digitados foram: {princ[1]}')