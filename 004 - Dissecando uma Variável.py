palavra = input('Digite uma palavra: ')
print('O tipo primitivo desse valor é' , type(palavra)) #Tipo de Carácter
print('Só tem espaços', palavra.isspace()) #Para verificar se tem espaços
print('É um número? ', palavra.isnumeric()) #Para verificar se é numérico
print('É alfabético? ', palavra.isalpha()) #Para verificar se é alfabético
print('É alfa numérico? ', palavra.isalnum()) #Para verificar se é alfa numérico
print('Está em maiúsculas?', palavra.isupper())#Para verificar se está em letras maiúsculas
print('Está em minúsculas?', palavra.islower())#Para verificar se está em letras minúsculas
print('Está capitalizada?', palavra.istitle())#Para verificar está capitalizada
