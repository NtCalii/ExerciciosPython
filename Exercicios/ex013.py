#

salario = float(input("Qual é o sálario do funcionário: "))
novoSalario = salario + (salario * 15 / 100)
print(f"Um funcionário que ganhava {salario:.2f}, com 15% de aumento, passa a receber {novoSalario:.2f}")
