# n = 1
# while n != 0:
#     n = int(input('Digite em valor: '))
# print('FIM!')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar ? [S/N]')).upper()
# print('Fim!')

# n = 1
# par = impar = 0 # Pode fazer assim também para os valores que irão resular o mesmo resultado. 
# while n != 0:
#     n = int(input('Digite um valor: '))
#     if n != 0:
#         if n % 2 == 0:
#             par += 1
#         else:
#             impar += 1
# print(f'Você digitou {par} números pares e {impar} números ímpares!')

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Informe o seu sexo: [M/F]')).upper() # Upper para deixar a letra maiúscula. 
while sexo not in 'MmFF':
  sexo = str(input('Dados inválidos. Por favor, informe o sexo corretamente: ')).upper()  
print(f'Sexo {sexo} registrado com sucesso!')