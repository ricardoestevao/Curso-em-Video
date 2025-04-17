n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 4.9:
        print('O aluno(a) tirou {} de média e está REPROVADO(a)!'.format(media))
elif 5 <= media <= 6.9:
    print('O aluno(a) tirou {} de média e está de RECUPERAÇÃO'.format(media))
elif media >= 7:
    print('O aluno(a) tirou {} de média e está APROVADO!'.format(media))

