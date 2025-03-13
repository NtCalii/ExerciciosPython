'''Faça um programa que leia um sálario de um funcionário e calcule o valor do aumento.
Para sálario superior a R$1250,00 calcule o valor de 10% de aumento.
Para sálarios inferiores o aumento é de 15%.'''

salario = float(input("Qual o salário do funcionário? R$"))
if salario <= 1250:
    print(f"Quem ganhava R${salario} passa a ganhar {(salario * 15) / 100} agora.")
else:
    print(f"Quem ganhava R${salario} passa a ganhar {salario + (salario * 10) / 100} agora.")
