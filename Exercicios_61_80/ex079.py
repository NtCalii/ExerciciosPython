'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente. '''

lista = []
continuar = "S"
while continuar == "S":
    n1 = int(input("Digite um valor: "))
    if n1 not in lista:
        lista.append(n1)
        print("Valor adicionado.")
    else:
        print("Valor duplicado! Não vou adicionar.")
    continuar = input("Deseja continuar? [S/N]: ").upper()
print("=-=" * 10)
lista.sort()
print(f"Você digitou os valores {lista}")
