# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg): # Função que recebe uma mensagem e imprime com bordas
    tam = len(msg) + 4 # Calcula o tamanho da borda com base no tamanho da mensagem
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)

# Programa principal
escreva('Ricardo')
escreva('Ricardo Santos Estevão da Silva')
escreva('Dia vinte e sete de maio de dois mil e vinte e cinco')