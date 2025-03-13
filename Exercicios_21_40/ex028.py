'''Escreva um programa que faça o computador escolher um número entre 0 e 5 e peça para o usuário
tentar adivinhar o número que o computador escolheu.'''

from random import randint
from time import sleep

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
      "Vou pensar em um número entre 0 e 5. Tente adivinhar...\n"
      "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n1 = randint(0, 5)
print("ESCOLHENDO...")
sleep(2)
resp = int(input("Qual número eu pensei? "))
if resp == n1:
    print(f"EEBAAA!!!, você acertou, o número que pensei foi {n1}")
else:
    print(f"Que pena, você errou, o número que pensei foi {n1}")
