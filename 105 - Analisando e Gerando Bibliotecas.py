# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:


# Programa Principal

def notas (*n, sit=False): # *n significa que pode receber várias notas
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: notas dos alunos (pode receber várias notas)
    :param sit: (opcional) se True, retorna a situação da média das notas
    :return: dicionário com total de notas, maior nota, menor nota, média das notas e situação (se sit for True)
    """
    r = dict() # dicionário para armazenar os resultados
    r['total'] = len(n) # total de notas
    r['maior'] = max(n) # maior nota
    r['menor'] = min(n) # menor nota
    r['média'] = sum(n)/len(n) # média das notas
    # se sit for True, adiciona a situação    
    if sit:
        if r['média'] >=7: # se média maior ou igual a 7
            r['situação'] = 'BOA' # situação é boa
        elif r['média'] >=5: # se média maior ou igual a 5
            r['situação'] = 'RAZOÁVEL' # situação é razoável
        else: # se média menor que 5
            r['situação'] = 'RUIM' # situação é ruim
    return r # retorna o dicionário com os resultados

resp = notas(9, 7, 10, 2.5, 8.5, sit=True)  # True significa que quer a situação
#print(resp)
help(notas)  # ajuda para ver como usar a função