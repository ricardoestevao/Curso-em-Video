#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(4):
    print(f'----- {i + 1}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

print(f'\nA média de idade do grupo é de {media_idade:.1f} anos.')
if homem_mais_velho:
    print(f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {homem_mais_velho}.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo, há {mulheres_menos_20} mulher(es) com menos de 20 anos.')