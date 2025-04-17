salario = float(input('Qual é o salário do funcionário? R$ '))
if salario > 1250:
    print('O seu aumento foi de 10% (R${:.2f}), por tanto receberá {}'.format((salario*0.10), (salario*0.10)+salario))
else:
    print('O aumento foi de 15% (RS {:.2f}), por tanto receberá {}'.format((salario*0.15), (salario*0.15)+salario))