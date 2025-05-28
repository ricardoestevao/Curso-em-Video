# # vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# # Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

# dados = {'nome':'Ricardo','idade':30} # Difirente de listas e tuplas o dicionário usa o nome como elemento e não números.
# print(dados['nome'])
# print(dados['idade'])

# # Para adicionar um novo dado na variável desejada não se usa o .append() apenas escreva o que se quer adiconar Ex:
# dados['Sexo']='M'
# print(dados['Sexo'])

# # Para excluir algum dado dentro do dicionário usa-se o comando 'del' conforme exemplo abaixo:
# del dados['idade']

# Mais exemplos de cada funciona o dicionário.
# filme = {'titulo':'Star Wars',
#  'ano':1997,
#  'diretor':'George Lucas'

# }
# print(filme)

# # Diferença entre valores, chaves e itens.
# print(filme.values()) # Irar apresentar todos os valores do dicionário.
# print(filme.keys()) # Irar apresentar todos os titulos do dicionário.
# print(filme.items()) # Irar apresentar tanto os valores e titulos do dicionário.

# # __________________________________________________________________________________

# for k, v in filme.items():
#     print(f'O {k} é {v}')

# #____________________________________________________________________________________

# pessoas = {'Nome':'Ricardo','Sexo':'M', 'Idade': 30}
# print(pessoas) # Irar aparecer todos os dados e elementos.
# print(pessoas['Nome']) # Ira apresentar o elemento nome
# print(pessoas['Idade']) # Irar apresentar o elemento idade
# print(pessoas['Sexo']) # Irar apresentar o elemento Sexo
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos') # Print formatado para apresentar os dados solicitados
# print(pessoas.keys()) # Irar apresentar todos os titulos do dicionário.
# print(pessoas.values()) # Irar apresentar todos os valores do dicionário.
# print(pessoas.items()) # Irar apresentar tanto os valores e titulos do dicionário.

# #_____________________________________________________________________________________

# pessoas = {'Nome':'Ricardo','Sexo':'M', 'Idade': 30}
# for k in pessoas.keys(): # Irar apresentar as 'Chaves' do dicionário
#     print(k)

# pessoas = {'Nome':'Ricardo','Sexo':'M', 'Idade': 30}
# for k in pessoas.values(): # irar apresentar os "Valores" do dicionário
#     print(k)

# pessoas = {'Nome':'Ricardo','Sexo':'M','Idade':30}
# for k, i in pessoas.items(): # Parecido com o o Enumerate que é usado nas tuplas e listas, porém no dicionário é assim que se apresenta.
#     print(f'{k} = {i}')
# #______________________________________________________________________________________
# # Criando um dicionário dentro de uma lista

# brasil = [] # lista
# estado1 = {'UF':'Rio de Janeiro', 'Sigla':'RJ'} # Dicionário
# estado2 = {'UF':'São Paulo','Sigla': 'SP'} # Dicionário
# brasil.append(estado1) # Adicionando o dicionário estado1 dentro da lista brasil
# brasil.append(estado2) # Adicionando o dicionário estado2 dentro da lista brasil

# print(brasil)  # irar apresentar o que foi adiciona dentro da lista brasil

# brasil = [] # lista
# estado1 = {'UF':'Rio de Janeiro', 'Sigla':'RJ'} # Dicionário
# estado2 ={'UF':'São Paulo','Sigla': 'SP'} # Dicionário
# brasil.append(estado1) # Adicionando o dicionário estado1 dentro da lista brasil
# brasil.append(estado2) # Adicionando o dicionário estado2 dentro da lista brasil

# print(brasil[0]) # Irar apresentar apenas o elemento 0 da lista que foi adicionado

# brasil = [] # lista
# estado1 = {'UF':'Rio de Janeiro', 'Sigla':'RJ'} # Dicionário
# estado2 ={'UF':'São Paulo','Sigla': 'SP'} # Dicionário
# brasil.append(estado1) # Adicionando o dicionário estado1 dentro da lista brasil
# brasil.append(estado2) # Adicionando o dicionário estado2 dentro da lista brasil

# print(brasil[1]) # Irar apresentar apenas o elemento 1 da lista que foi adicionado

# brasil = [] # lista
# estado1 = {'UF':'Rio de Janeiro', 'Sigla':'RJ'} # Dicionário
# estado2 ={'UF':'São Paulo','Sigla': 'SP'} # Dicionário
# brasil.append(estado1) # Adicionando o dicionário estado1 dentro da lista brasil
# brasil.append(estado2) # Adicionando o dicionário estado2 dentro da lista brasil

# print(brasil[0]['UF']) # Brasil 0, elemento 'UF' = Rio de Janeiro
# #________________________________________________________________________________

# estado = dict() # dicionário
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['Silga'] = str(input('Sigla do Estado:'))
#     brasil.append(estado.copy()) # Para fazer uma copia de uma lista com o dicionário usa-se o comando 'copy'
# print(brasil)
#__________________________________________________________________________________

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# aluno = dict() # dicionário
# aluno['Nome'] = str(input('Nome: '))
# aluno['média'] = float(input(f'Média de {aluno["Nome"]}: '))
# if aluno['média'] >= 7:
#     aluno['Situação'] = 'Aprovado'
# elif 5 <= aluno['média'] < 7:
#     aluno['Situação'] = 'Recuperação'
# else:
#     aluno['Situação'] = 'Reprovado'

# print(aluno)