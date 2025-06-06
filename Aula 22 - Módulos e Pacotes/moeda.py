def metade(preço):
    res = preço / 2
    return f'R$ {res:.2f}'


def dobro(preço):
    res = preço * 2
    return f'R$ {res:.2f}'


def aumento(preço, taxa):
    res = preço + (preço * taxa/100)
    return f'R$ {res:.2f}'


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return f'R$ {res:.2f}'

def resumo(preço, taxa1, taxa2):
    print(f'A metade de R$ {preço:.2f} é {metade(preço)}')
    print(f'O dobro de R$ {preço:.2f} é {dobro(preço)}')
    print(f'O aumento de {taxa1}% é de {aumento(preço, taxa1)}') 
    print(f'O desconto de {taxa2}% é de {diminuir(preço, taxa2)}')