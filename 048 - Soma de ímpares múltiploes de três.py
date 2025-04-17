soma = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:  # Verifica se é ímpar e múltiplo de 3
        soma += numero

print(f'A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é: {soma}')