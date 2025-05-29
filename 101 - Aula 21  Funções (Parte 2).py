from time import sleep
# def contador (i, f, p): #Função que recebe três parâmetros: início, fim e passo
#     """
#     -> Faz uma contagem e mostra na tela."""
#     c = i # Inicializa o contador com o valor de início
#     while c <= f: # Enquanto o contador for menor ou igual ao fim
#         sleep(0.2) # Pausa de 0.2 segundos para visualização
#         print(f'{c} ', end='', flush=True) # Imprime o valor atual do contador sem pular linha
#         c = c + p # Incrementa o contador pelo valor do passo
#     print(' FIM!')


# help(contador)

# docstring é um comentário que explica o que a função faz, para acessa-lo usamos o comando help() e aspas triplas.
#_________________________________________________________________________________________________________________________

# # Parâmetros opcionais
# def somar(a=0, b=0, c=0): # Função que recebe três parâmetros com valor padrão 0
#     """
#     -> Faz a soma de três valores e retorna o resultado."""
#     s = a + b + c # Soma os valores dos parâmetros
#     return s # Retorna o resultado da soma

# def somar(a, b, c=0): # Função que recebe três parâmetros obrigatórios
#   s = a + b + c # Soma os valores dos parâmetros
#   print(f'A soma vale {s}') # Imprime o resultado da soma

# somar(2, 3, 5) # Chamada da função com três argumentos
# somar(8, 4) # Chamada da função com dois argumentos (o terceiro será considerado 0 por padrão desde que o parâmetro seja definido como =0))   
#__________________________________________________________________________________________________________________________

# Escopo de variáveis 
# def teste():
#     x = 8 # Variável local, só existe dentro da função teste
#     print(f'Na função teste, x vale {x}') # Imprime o valor da variável local x dentro da função teste
#     print(f'Na função teste, n vale {n}') # Imprime o valor da variável global n dentro da função teste

# # Programa principal
# n = 2 # Variável global
# print(f'Na variável n temos o valor {n}') # Imprime o valor da variável global
# teste() # Chamada da função teste
# print(f'No progrma principal, x vale {x}') # Tenta imprimir o valor da variável local x fora da função teste, o que causará um erro porque x não existe no escopo global

# def funcao():
#     n1 = 4 # Variável local, só existe dentro da função funcao
#     print(f'Na variavel local, n1 vale {n1}') # Imprime o valor da variável local n1 dentro da função funcao
    
# # Programa principal
# n1 = 2 # Variável global
# funcao() # Chamada da função funcao
# print(f'Na variável global n1 temos o valor {n1}') # Imprime o valor da variável global n1

# def somar(a=0, b=0, c=0): # Função que recebe três parâmetros com valor padrão 0
#     s = a + b + c # Soma os valores dos parâmetros
#     return s # Retorna o resultado da soma

# # Programa principal
# r1 = somar(2, 3, 5) # Chamada da função com três argumentos
# r2 = somar(8, 4) # Chamada da função com dois argumentos (o terceiro será considerado 0 por padrão)
# r3 = somar(6) # Chamada da função com um argumento (os outros dois serão considerados 0 por padrão)

# print(f'Os resultados foram {r1}, {r2} e {r3}') # Imprime os resultados das chamadas da função somar