# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#O primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.





def fatorial (n, show=False): # Função que calcula o fatorial de um número
       """
    Calcula o fatorial de um número.
    
    Parâmetros:
    n -- número inteiro a ser calculado o fatorial
    show -- (opcional) mostrar ou não o processo de cálculo

    Retorna:
    O valor do fatorial de n.
    """
    f = 1 # Inicializa o fatorial como 1
    for c in range(n, 0, -1): # Percorre de n até 1
        if show: # Se show for True, exibe o processo de cálculo
            print(f'{c}', end='') # Exibe o número atual
            if c > 1: # Se não for o último número, exibe o símbolo de multiplicação
                print(' x ', end='') # Exibe o símbolo de multiplicação
            else: # Se for o último número, exibe o sinal de igual
                print(' = ', end='') # Exibe o sinal de igual
        f *= c # Multiplica o fatorial pelo número atual
    return f # Retorna o valor do fatorial calculado

#Programa principal
print(fatorial(5, show=True)) # Exemplo de uso da função fatorial com o parâmetro show como True


