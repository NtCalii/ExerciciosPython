'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o.'''

n1 = 0
for c in range(1, 7):
    n2 = int(input("Digite um número: "))
    if n2 % 2 == 0:
        n1 = n1 + n2
print(f"A soma de todos os números pares são {n1}")
