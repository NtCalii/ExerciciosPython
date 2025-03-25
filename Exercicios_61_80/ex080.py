'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for c in range(0, 5):
    n1 = int(input("Digite um valor: "))
    if c == 0:
        lista.append(n1)
    elif n1 >= max(lista):
        lista.append(n1)
    elif n1 <= min(lista):
        lista.insert(0, n1)
    else:
        lista.insert(n1)
print("=-=" * 10)
print(f"Os valores digitados foram {lista}")
