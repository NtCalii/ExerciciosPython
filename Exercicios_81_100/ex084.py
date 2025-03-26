'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dados = []
pessoa = []
maior = menor = 0
nomeMaior = nomeMenor = ""
while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    pessoa.append(dados[:])
    dados.clear()
    continuar = input("Quer continuar [S/N]: ").upper()
    if continuar == "N":
        break
print("=-=" * 15)
for p in pessoa:
    if maior == 0:
        maior = p[1]
        menor = p[1]
    if p[1] > maior:
        maior = p[1]
        nomeMaior = p[0]
    if p[1] < menor:
        menor = p[1]
        nomeMenor = p[0]
print(f"Ao todo você cadastrou {len(pessoa)}\n"
      f"O maior peso foi de {maior:.2f}Kg. Peso de {nomeMaior}\n"
      f"O menor peso foi de {menor:.2f}Kg. Peso de {nomeMenor}")
