from datetime import datetime
dados = dict()  # Criando um dicionário vazio para armazenar os dados dos trabalhadores
dados['nome'] = str(input('Nome: ')) # Solicitando o nome do usúario
nasc = int(input('Ano de Nascimento: ')) # Solicitando a data de nascimento do usúario
dados['idade'] = datetime.now().year - nasc # Solocitando o ano de nascimento do usuário
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): ')) # Número da carteira de trabalho, caso não tiver o usuário clica 0 e encerrará o programa. 
if dados['ctps'] != 0: # Criando uma estrutura condicional
    dados['contratação']= int(input('Ano de contratação: ')) # Adicionando o ano de contratação dentro da estrutura
    dados['salário'] = float(input('Salário: R$')) # Adicionando o salário do usuário dentro da estrutura
    dados['aposentadoria'] = dados ['idade'] + ((dados['contratação'] + 35) - datetime.now().year) # Adicionando a idade de aposentadoria do usuário
print('-=-' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
