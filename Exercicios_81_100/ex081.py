'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = input("Quer continuar? [S/N]: ").upper()
    if continuar == "N":
        break
print("=-=" * 10)
lista.sort(reverse=True)
print(f"Você digitou {len(lista)}.\n"
      f"Os valores em ordem decresente são {lista}\n"
      f"O valor 5 ", end="")
if 5 in lista:
    print("Faz parte da lista." )
else:
    print("Não faz parte da lista.")
