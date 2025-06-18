# def leiaInt(msg): # Função para ler um número inteiro
#     """Função para ler um número inteiro do usuário.
#     Args:
#         msg (str): Mensagem a ser exibida ao usuário.
#     Returns:
#         int: O número inteiro digitado pelo usuário.
#     """
#     while True: # Loop infinito para garantir que o usuário digite um número válido
#         try: # Tenta converter a entrada do usuário para um inteiro
#             n = int(input(msg)) # Solicita ao usuário um número inteiro
#         except (ValueError, TypeError): # Captura erros de conversão de tipo
#             print('ERRO: por favor, digite um número inteiro válido') 
#             continue # Continua o loop se ocorrer um erro
#         else: # Se a conversão for bem-sucedida, sai do loop
#             return n # Retorna o número inteiro digitado pelo usuário





# num = leiaInt('Digite um valor: ') # Chama a função leiaInt para ler um número inteiro do usuário
# print(f'O valor digitado foi {num}') # Exibe o número digitado pelo usuário

num = [3, 6, 4, 1]

for n1, n2 in enumerate(num):
    print(n1 + n2)