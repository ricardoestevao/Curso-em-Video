# Crie um módulo chamado moeda.py que tenha as funções incorporadas 
# aumentar(), 
# diminuir(),
# dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# Programa principal
import moeda

pr = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {pr} é {moeda.metade(pr)}')
print(f'O dobro de {pr} é {moeda.dobro(pr)}')
print(f'O aumento de 10% {pr} é {moeda.aumento(pr, 10)}')
print(f'O desconto de 15% de {pr} é {moeda.diminuir(pr, 15)}')