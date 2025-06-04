import uteis # Importa o módulo uteis, que deve conter funções úteis como fatorial e dobro
# Importante: O módulo uteis deve estar no mesmo diretório ou no caminho do Python para ser importado corretamente.

# Modularização - O Ato de construir módulos, onde iremos dividir parte do programa. 
# Vantagens da modularização - # 1. Reutilização de código: Podemos usar o mesmo módulo em diferentes programas sem precisar reescrever o código.
# 2. Organização: Facilita a organização do código, separando funcionalidades em arquivos distintos.
# 3. Manutenção: Facilita a manutenção do código, pois alterações em um módulo não afetam outros módulos diretamente.
# 4. Colaboração: Permite que diferentes desenvolvedores trabalhem em diferentes módulos simultaneamente.
# 5. Testabilidade: Facilita a criação de testes unitários para cada módulo individualmente.
# 6. Escalabilidade: Permite que o código cresça de forma mais controlada e estruturada.
# 7. Legibilidade: Melhora a legibilidade do código, tornando-o mais fácil de entender e seguir.    

#_____________________________________________________________________________________________________________________________________________

# Pacote - # É um diretório que contém vários módulos relacionados.
# Exemplo: Um pacote pode conter módulos para manipulação de arquivos, conexão com banco de dados, etc.

num=int(input("Digite um valor: ")) # Solicita ao usuário um número inteiro
fat=uteis.fatorial(num) # Chama a função fatorial com o número fornecido pelo usuário
print(f'O fatorial de {num} é {fat}') # Exibe o resultado do fatorial calculado
print(f'O dobro de {num} é {uteis.dobro(num)}')
# O código acima define uma função para calcular o fatorial de um número e a utiliza para calcular o fatorial de um número fornecido pelo usuário.