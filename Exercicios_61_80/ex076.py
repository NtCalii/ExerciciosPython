'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ("Lápis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 20,
            "Mochila", 99.90,
            "Canetas", 22.30,
            "Livros", 34.90)
print("-=-" * 20)
print("                   LISTAGEM DE PREÇOS")
print("-=-" * 20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:.>7.2f}")
print("-=-" * 20)
