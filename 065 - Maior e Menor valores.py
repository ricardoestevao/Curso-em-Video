# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else: 
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0] # [0] irar registrar apenas o primeira letra da respota ex: Sim ou Não vai resgitar apenas o S ou N. 
média = soma / quant
print(f'Você digitou {quant} e a média foi de {média} ')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
