'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(jogador="", gols=""):
    if jogador == "":
        jogador = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")

jogador = input("Nome do jogador: ")
gols = input("Número de gols: ")
ficha(jogador, gols)
