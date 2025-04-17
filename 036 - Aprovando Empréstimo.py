#Condições Aninhadas - Aula 12
#
# nome = str(input('Qual é o seu nome? '))
# if nome == 'Ricardo':
#     print('Que nome LINDO!')
# elif nome == 'Maria' or nome == 'José' or nome == 'João': # Or significa 'OU' - O elif pode se usar quantas vezes desejar.
#     print('Seu nome é bem popular!')
# else: # Com o uso elif o else se torna opção.
#     print('Seu nome é bem normal')
# print('Tenha um bom dia, {}'.format(nome))

#Desafios

casa = float(input('Qual é o valor da imóvel? R$ '))
salario = float(input('Qual é o salário do comprador? '))
anos = int(input('Em quantos anos deseja pagar o imóvel? '))
porcento = salario * 0.30
valor_da_prestação = casa / (anos * 12)
print('Para pagar uma casa de R$ {}, em {} anos a prestação será de {:.2f}'.format(casa, anos, valor_da_prestação))
if valor_da_prestação > porcento:
    print('Empréstimo NEGADO!')
elif valor_da_prestação < porcento:
    print('Empréstimo APROVADO!')

