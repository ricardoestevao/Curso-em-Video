# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    
    num = int(input('Quer ver a tabuada de qual valor? (Ou digite qualquer número negativo para sair do programa.)'))
    if num < 0:
       break
    print('-'*40)
    for c in range (1, 11):
        print(f'{num} x {c:2} = {num*c}')
    print ('-'*40)
    
print('Fim! ')