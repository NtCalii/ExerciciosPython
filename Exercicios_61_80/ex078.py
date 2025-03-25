'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
maior e o menor valor digitado.'''

valor = []
for v in range(0, 5):
    valor.append(int(input(f"Digite um valor para a posição {v}: ")))
print("=-=" * 10)
print(f"Você digitou os valores {valor}")
print(f"O maior valor digitado foi {max(valor)} nas posições ")
print(f"O menor valor digitado foi {min(valor)} nas posições ")
