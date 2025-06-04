#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def ajuda(comando):
    """
    -> Função para exibir o manual de um comando Python.
    :param comando: comando Python para o qual se deseja ver o manual
    """
    help(comando)

comando = '' # inicializa comando como vazio
while True:
        comando = str(input('\033[1;34mDigite o comando que deseja ver o manual (ou "FIM" para sair): \033[m')).strip().lower()
        if comando == 'fim':
            print('\033[1;31mSaindo do sistema de ajuda. Até logo!\033[m')
            break
        else:
            ajuda(comando)  # chama a função ajuda para exibir o manual do comando