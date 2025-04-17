print('============== LOJAS ESTEVÃO ==============')
compras = float(input('Preço das compras: R$ '))
print('FORMA DE PAGAMENTO')
print('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    print('Sua compra de R$ {} vai custar R$ {} no final'.format(compras,(compras - (compras * 0.10))))
elif opção == 2:
    total = compras - (compras * 5/100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(compras, total))
elif opção == 3:
    total = compras / 2
    print('Sua compra de R$ {:.2f} será parcelada em 2x no cartão de crédito no valor de {:.2f}'.format(compras, total))
elif opção == 4:
    totparc = int(input('Quantas parcelas? '))
    parcela = compras / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(totparc, parcela))
else: 
    total = 0
    print('Opção invalida de pagamento. Tente novamente! ')