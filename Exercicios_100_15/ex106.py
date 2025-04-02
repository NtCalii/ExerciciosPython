'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.'''

def mini_sistema_ajuda():
    """
    Mini-sistema interativo que utiliza o Interactive Help do Python.
    O usuário digita um comando e o manual correspondente é exibido.
    O programa encerra quando o usuário digita 'FIM'.
    """
    while True:
        comando = input("Digite o comando ou 'FIM' para sair: ").strip()
        if comando.upper() == 'FIM':
            print("Encerrando o sistema de ajuda.")
            break
        elif comando:
            help(comando)
        else:
            print("Por favor, digite um comando ou 'FIM'.")

if __name__ == "__main__":
    mini_sistema_ajuda()
