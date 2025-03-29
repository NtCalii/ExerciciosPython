'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.'''

jogador = {}
time = []
partidas = 0
continuar = ""

while True:
    jogador["nome"] = input("Nome: ")
    partidas = int(input(f"Quantas partidas o jogador {jogador['nome']} jogou? "))
    jogador["gols"] = []

    for cont in range(0, partidas):
        gols_partida = int(input(f"Quantos gols na partida {cont}: "))
        jogador["gols"].append(gols_partida)

    jogador["total"] = sum(jogador["gols"])

    time.append(jogador.copy())

    continuar = input("Deseja adicionar mais um jogador [S/N]: ").upper()
    if continuar == "N":
        break

print("=-=" * 25)
print("cod   nomes         gols    total\n"
      "---------------------------------")
for k, v in enumerate(time):
    print(f"{k}:>3", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("=-=" * 25)
