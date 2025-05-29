# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

print('-' * 30)

def voto (ano): # Função que verifica a idade e o tipo de voto
    idade = date.today().year - ano # Calcula a idade com base no ano de nascimento
    if idade < 16: # Verifica se a idade é menor que 16 anos
        return f'Com {idade} anos: NÃO VOTA' # Voto NEGADO
    elif 16 <= idade <18 or idade > 65: # Verifica se a idade está entre 16 e 17 anos ou é maior que 65 anos
        return f'Com {idade} anos: VOTO OPCIONAL' # Voto OPCIONAL
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.' # Voto OBRIGATÓRIO

# Programa Principal

print(voto(2015))