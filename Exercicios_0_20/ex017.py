#Faça um programa que leia o cateto oposte e adjacente de um triângulo retângulo, calcule o comprimento
#da hipotenusa.

from math import hypot

catetoOp = float(input("Comprimento do cateto oposto: "))
catetoAd = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(catetoAd, catetoOp)
print(f"A hipotenusa vai medir: {hipotenusa:.2f}")
