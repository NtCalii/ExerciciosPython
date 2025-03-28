'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

rank = []
jogo = {"Jogador 1": randint(1, 20),
        "Jogador 2": randint(1, 20),
        "Jogador 3": randint(1, 20),
        "Jogador 4": randint(1, 20)
        }
print("VALORES SORTEADOS")
for k, v in jogo.items():
    print(f"{k} tirou {v} no d20.")
    sleep(1)
print("=-=" * 10)
print("RANKING VENCEDORES")
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f"Em {i + 1} lugar: {v[0]} com {v[1]}")
    sleep(1)
