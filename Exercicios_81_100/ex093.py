'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em
cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.'''

jogador = {}
partidas = 0
jogador["nome"] = input("Nome: ")
partidas = int(input(f"Quantas partidas o jogador {jogador['nome']} jogou? "))
jogador["gols"] = []

for cont in range(0, partidas):
    gols_partida = int(input(f"Quantos gols na partida {cont}: "))
    jogador["gols"].append(gols_partida)

jogador["total"] = sum(jogador["gols"])

print("=-=" * 25)
print(jogador)
print("=-=" * 25)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor de {v}")

print("=-=" * 25)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

for i, gols in enumerate(jogador["gols"]):
    print(f"  => Na partida {i}, fez {gols} gols.")

print(f"Foi um total de {jogador['total']} gols.")
