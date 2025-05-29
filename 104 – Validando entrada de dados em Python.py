# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg): # Função para ler um número inteiro com validação
    while True: # Loop infinito para garantir a validação
        valor = input(msg) # Solicita ao usuário um valor
        if valor.isnumeric(): # Verifica se o valor é numérico
            return int(valor) # Converte o valor para inteiro e retorna
        else: # Se o valor não for numérico, exibe mensagem de erro
            print('\033[31mERRO! Digite um número inteiro válido.\033[m') 

# Programa principal
n = leiaInt('Digite um número: ') 
print(f'Você acabou de digitar o número {n}.')