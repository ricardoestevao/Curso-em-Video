n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O PRIMEIRO número é maior')
elif n1 < n2:
    print('O SEGUNDO número é maior')
else:
    var = n1 == n2
    print('Os números são IGUAIS')