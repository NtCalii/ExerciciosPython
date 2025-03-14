'''Faça um programa que leia um número inteiro e paça para o úsuariao escolher qual será a base de
conversão'''

n1 = int(input("Digite um número que você queira converter: "))
print(" [1] Converter para BINÁRIO\n [2] Converter para OCTAL\n [3] Converter para EXADECIMAL")
n2 = int(input("Sua opção: "))
if n2 == 1:
    print(f"O número {n1} em binário é {bin(n1)[2:]}")
elif n2 == 2:
    print(f"O número {n1} em octal é {oct(n1)[2:]}")
elif n2 == 3:
    print(f"O número {n1} em exadecimal é {hex(n1)[2:]}")
else:
    print("Opção inválida.")
