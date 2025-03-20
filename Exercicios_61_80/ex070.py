'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

continuar = "S"
nomeP = nomeB = ""
valorP = totalC = contMil = menorPreço = 0

print("-=-" * 10)
print("     LOJA SUPER BARATÃO")
print("-=-" * 10)

while continuar == "S":
    nomeP = input("Qual o nome do produto: ")
    valorP = float(input("Qual o preço do produto R$"))
    if valorP >= 1000:
        contMil += 1
    if totalC == 0:
        menorPreço = valorP
    if valorP < menorPreço:
        menorPreço = valorP
        nomeB = nomeP
    totalC = totalC + valorP
    continuar = input("Quer continuar [S/N]: ").strip().upper()

print("-=-" * 5, end="")
print("FIM DO PROGRAMA", end="")
print("-=-" * 5)
print(f"O total da compra foi R${totalC}\n"
      f"Temos {contMil} produto custando mais de R$1.000\n"
      f"O produto mais barato foi {nomeB} custando R${menorPreço}")
