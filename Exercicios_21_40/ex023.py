'''Faça um programa que leia um número de 0 a 9999 e mostre na tela coada separado
ex: digite um número..., unidade... dezena... centena... milhar...'''

import srt

n1 = int(input("DIgite um número: "))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f"Analisando o número {n1}\n"
      f"Unidade: {u}\n"
      f"Dezena: {d}\n"
      f"Centena: {c}\n"
      f"Milhar: {m}\n")
