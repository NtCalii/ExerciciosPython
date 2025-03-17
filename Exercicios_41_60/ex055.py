'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
peso lidos.'''

maior = 0
menor = 0
for c in range(1, 6):
    n1 = float(input(f"Peso da {c} pessoa: "))
    if c == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
print(f"O maior peso foi de {maior:.1f}Kg\n"
      f"O menor peso foi de {menor:.1f}Kg")
