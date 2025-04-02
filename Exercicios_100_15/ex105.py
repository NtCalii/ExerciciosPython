'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas de alunos (aceita várias).
    :param sit: valor opcional, se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação dos alunos.
    '''
    r = {}
    r["Total"] = len(n)
    r["Maior"] = max(n)
    r["Menor"] = min(n)
    r["Média"] = sum(n)/len(n)
    if sit:
        if r["Média"] >= 7:
            r["Situação"] = "Boa"
        elif r["Média"] >= 5:
            r["Situação"] = "Razoável"
        else:
            r["Situação"] = "Ruim"
    return r

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
