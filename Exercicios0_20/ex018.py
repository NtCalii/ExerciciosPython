#Faça um programa que leia um ângulo e mostre o valor de seno, cosseno e tangente.

from math import cos, sin, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))
print(f"O ângulo de {angulo} tem o SENO de {sin(radians(angulo)):.2f}\n"
      f"O ângulo de {angulo} tem o COSSENO de {cos(radians(angulo)):.2f}\n"
      f"O ângulo de {angulo} tem a TANGENTE de {tan(radians(angulo)):.2f}\n")
