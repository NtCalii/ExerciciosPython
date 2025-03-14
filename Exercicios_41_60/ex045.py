'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from time import sleep
from random import choice

computador = choice([1, 2, 3])
print("Suas opções.\n"
      "[1] PEDRA\n"
      "[2] PAPEL\n"
      "[3] TESOURA")
jogador = int(input("Qual a sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
print("-=-" * 10)
print(f"COMPUTADOR JOGOU {computador}")
print(f"JOGADOR JOGOU {jogador}")
print("-=-" * 10)
if jogador == computador:
    print("EMPATE!!!")
elif jogador == 1 and computador == 3:
    print("Jogador VENCEU!!!")
elif jogador == 2 and computador == 1:
    print("Jogador VENCEU!!!")
elif jogador == 3 and computador == 2:
    print("Jogador VENCEU!!!")
else:
    print("Computador VENCEU!!!")
