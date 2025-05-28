def mostrarLinha(): # DEF "Definição de Função" - "Mostrar Linha" é o nome que dei a função que é o print. Definição sem parâmetro
    print('-=-' * 10)

# # Programa Principal
# mostrarLinha()
# print('     SISTEMA DE ALUNOS       ')
# mostrarLinha()
# mostrarLinha()
# print('     CADASTRO DE FUNCIONÁRIOS        ')
# mostrarLinha()
# mostrarLinha()
# print('     ERRO DE SISTEMA     ')
# mostrarLinha()

# def título(txt): # Definição com parâmetro
#     mostrarLinha()
#     print(txt)
#     mostrarLinha()


# # Programa Principal
# título('    CURSO EM VIDEO      ')
# título('    PYTHON É MUITO BOM! ')
# título('    OPA, TESTE!      ')

# _________________________________________________________________________________________________________________

# def soma (a, b): # Definindo a função soma com dois parâmetros (a, b) onde 's' recebe o valor de a + b como resultado. 
#     s = a + b
#     print(s)

# # Programa Principal
# soma(4, 6)
# soma(10, 10)
# soma(15, 15)

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')

# # Programa Principal
# soma(4, 5)
# soma(7, 6,)

#___________________________________________________________________________________________________________________

# Empacotamento = O processo de empacotar vários valores em uma tupla.

# def contador(*num):  # Definição de função com empacotamento, onde num é uma tupla que recebe vários valores e o * indica o desempacotamento.
#     tam = len(num)  # Calcula o tamanho da tupla num.
#     print(f'Recebido os valores {num} com {tam} elementos.')
# # Programa Principal
# contador(5, 7, 3, 1, 4) 
# contador(8, 4, 7)

# def dobra(lst): # Definição de função que recebe uma lista como parâmetro e dobra cada elemento da lista.
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1

# valores = [6, 3, 9, 10, 2] # Lista de valores a serem dobrados.
# dobra(valores) 
# print(valores) # Exibe a lista de valores após a função dobra ter sido aplicada.

# def soma(*valores): # Definição de função que recebe vários valores e retorna a soma deles
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} temos {s}') # Exibe a soma dos valores recebidos.
# # Programa Principal
# soma(5, 2) # Chamada da função soma com dois valores.
# soma(2, 9, 4) # Chamada da função soma com três valores.