d = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} na frase'.format(d.count('A')))#Função Count para pesquisar a primeira letra desejada
print('A primeira letra A aparece na posição {}'.format(d.find('A')+1)) # Soma se +1 por causa do primeiro carácter não entrar
print('A ultima letra A aparece na posição {}'.format(d.rfind('A')+1))