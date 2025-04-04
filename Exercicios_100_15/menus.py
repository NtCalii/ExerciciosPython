'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em
um arquivo de texto simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

arq = "CursoEmVideo.txt"

def linha(tam=14):
    print("=-=" * tam)


def menuPricinpal(caso=0):
    print("             MENU PRINCIPAL")
    linha()
    print("[1] - Ver pessoas cadastradas\n"
          "[2] - Cadastrar nova Pessoa\n"
          "[3] - Sair do Sistema")
    linha()
    while True:
        try:
            resp = int(input("Sua Opção: "))
            if resp not in (1, 2, 3):
                raise ValueError
        except (ValueError, TypeError, KeyboardInterrupt):
            print("ERRO: por favor, digite uma opção válida.")
            linha()
        else:
            match resp:
                case 1:
                    linha()
                    print("            PESSOAS CADASTRADAS")
                    lerArquivo("CursoEmVideo.txt")
                    linha()
                case 2:
                    linha()
                    print("           CADASTRAR PESSOAS")
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    cadastrar(arq, nome, idade)
                case 3:
                    print("Saindo do Sistema... Até logo!")
                    break


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("ERRO ao ler o arquivo!")
    else:
        for l in a:
            dado = l.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo.")
    else:
        try:
            a.write(f"{nome}; {idade}\n")
        except:
            print("Houve um ERRO na hora de adicionar os dados.")
        else:
            print(f"Novo registro de {nome} adicionado.")
            linha()
            a.close()

