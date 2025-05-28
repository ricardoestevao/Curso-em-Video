# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(largura, comprimento): # Função que calcula a área do terreno
    total = largura * comprimento # Cálculo da área
    print(f'A área de um terreno {largura}x{comprimento} é de {total}m²') # Exibe o resultado

# Programa Principal
print('Controle de Terrenos')  
print('---------------------')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento) # Chama a função área com os valores de largura e comprimento