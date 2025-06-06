# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.

# Tratamento de Erros e Exceções no Python
# NameError: é uma "exceção" Erro que ocorre quando o nome de uma variável não é encontrado.
# Exemplo de de NameError:  print(x) - # Erro de NameError, pois a variável "x" não foi definida antes de ser usada.


# Erro de sintaxe é um erro que ocorre quando o código não está escrito corretamente.
# Exemplo de erro de sintaxe:
# primt("Hello World") - # Erro de sintaxe, pois "print" está escrito incorretamente.

# ValuerError: é um erro que ocorre quando uma função recebe um argumento com o tipo de dado errado.
# Exemplo de ValueError: int("Hello") - # Erro de ValueError, pois a função int() não pode converter uma string que não é um número em um inteiro.

# TypeError: é um erro que ocorre quando uma operação é realizada em um tipo de dado que não é suportado.
# Exemplo de TypeError: r = 2/'2' - # Erro de TypeError, pois a operação de divisão não pode ser realizada entre um número inteiro e uma string.

# ZeroDivisionError: é um erro que ocorre quando uma divisão por zero é tentada.
# Exemplo de ZeroDivisionError: r = 2/0 - # Erro de ZeroDivisionError, pois não é possível dividir um número por zero.

# IndexError: é um erro que ocorre quando um índice de uma lista ou tupla é inválido.
# Exemplo de IndexError: lista = [1, 2, 3]; print(lista[3]) - # Erro de IndexError, pois o índice 3 está fora do intervalo da lista. (a lista tem índices 0, 1 e 2)

# ModuleNotFoundError: é um erro que ocorre quando um módulo não é encontrado.
# Exemplo de ModuleNotFoundError: import modulo_inexistente - # Erro de ModuleNotFoundError, pois o módulo "modulo_inexistente" não existe.

#________________________________________________________________________________________________________________________________________________________________

# try: # Bloco de código que pode gerar uma exceção
#     a = int(input('Numerador: ')) # Solicita ao usuário um número inteiro para o numerador
#     b = int(input('Denominador: ')) # Solicita ao usuário um número inteiro para o denominador
#     r = a / b # Realiza a divisão do numerador pelo denominador
# except Exception as erro: # Captura qualquer exceção que ocorra no bloco try
#     print(f'Problema encontrado foi {erro.__class__}') # Exibe a classe da exceção encontrada
# else: # Se não ocorrer nenhuma exceção, este bloco será executado
#     print(f'O resultado é {r:.1}') # Exibe o resultado da divisão formatado com uma casa decimal
# finally: # Este bloco sempre será executado, independentemente de ocorrer ou não uma exceção
#     print('Volte sempre! Muito Obrigado!')
#________________________________________________________________________________________________________________________________________________________________
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except (ValueError, TypeError):
#     print('Tivemos um problema com os tipos de dados que você digitou.')

# except ZeroDivisionError:
#     print('Não é possivel dividir um número por zero!')

# except KeyboardInterrupt:
#     print('O usuário preferiu não informar os dados!')

# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito obrigado!')