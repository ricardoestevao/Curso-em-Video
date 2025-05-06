#As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

#--------------------------------------------------------------------------------------

# dados = list()
# dados.append('Pedro')
# dados.append(25)
# galera = list()
# galera.append(dados[:])
# dados[0]='Ricardo'
# galera[1]= 30
# galera.append(dados[:])
# print(galera)

#---------------------------------------------------------------------------------------

# galera = [['Ricardo', 30], ['Lucas', 10], ['Nair', 29], ['Casa',77]]
# print(galera [1:])

# galera = [['Ricardo', 30], ['Lucas', 10], ['Nair', 29], ['Casa',77]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

#----------------------------------------------------------------------------------------

# galera = list()
# dado = list() # Irar criar uma lista temporaria dentro de galera
# totmai = totmen = 0
# for c in range(0, 5):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:]) # Criando uma cópia de dado dentro de galera
#     dado.clear()# Limpando os dados da lista temporário dentro de galera

# for p in galera:
#     if p[1] >= 18: # Para sabermos dados de maiores de idade
#         print(f'{p[0]} é maior de idade.')
#         totmai += 1
#     else:
#         print(f'{p[0]} é menor de idade.')
#         totmen += 1

# print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')

#------------------------------------------------------------------------------------------

# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        mai = men = temp[1]    
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-' * 30)

print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}KG de', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'{[p[0]]}', end=' ')
print(f'O menor peso foi de {men} KG de', end=' ')
for p in princ:
    if p[1] == men:
        print(f'{[p[0]]}')