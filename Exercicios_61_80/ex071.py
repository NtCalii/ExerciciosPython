''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de
cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("=====" * 2)
print("BANCO CEV")
print("=====" * 2)

valor = int(input("Qual o valor você quer sacar: R$"))
total = valor
céd = 50
totalCéd = 0
while True:
    if total >= céd:
        total -= céd
        totalCéd += 1
    else:
        if totalCéd > 0:
            print(f"Total de {totalCéd} cédulas de {céd}")
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalCéd = 0
        if total == 0:
            break
print("=====" * 2)
print("FIM")
