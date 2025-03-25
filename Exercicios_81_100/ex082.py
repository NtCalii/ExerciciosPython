'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista1 = []
listapar = []
listaimpar = []
while True:
    lista1.append(int(input("Digite um valor: ")))
    continuar = input("Quer continuar? [S/N]: ").upper()
    if continuar == "N":
        break
print("=-=" * 10)
for i, v in enumerate(lista1):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f"A lista completa {lista1}\n"
      f"A lista par {listapar}\n"
      f"A lista ímpar {listaimpar}")
