'''Faça um programa que leia o valor de uma casa, quanto o comprador ganha de salário e quantos anos
ele quer de financiamento. A prestação mensal, não pode exceder 30% do salário ou então o emprestimo
será negado.'''

casa = float(input("Qual o valor da casa: "))
salario = float(input("Qual o seu salário: "))
anos = int(input("Quantos anos quer financiar: "))
prestacao = casa / (anos * 12)
soma_por = (salario * 30) / 100
print(f"Para pagar uma casa de R${casa} em {anos} anos, a prestação será de R${prestacao:.2f}")
if soma_por <= prestacao:
    print(f"Empréstimo NEGADO!")
else:
    print(f"Empréstimo pode ser CONCEDIDO!")
