#Crie um programa que leia um número real e mostre na tela a sua porção inteira.
#Ex: digito 5.2453 e a saida é 5.

from math import trunc

n1 = float(input("Digite um valor: "))
porcaoInt = trunc(n1)
print(f"O valor digitado foi {n1} e a sua porção inteira é {porcaoInt}")
