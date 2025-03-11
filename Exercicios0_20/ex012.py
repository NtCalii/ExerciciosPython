#Faça um algoritmo que leia um e mostre o preço e calcule um desconte de 5% do produto.

preco = float(input("Qual o preço do produto: "))
precoDesconto = preco - (preco * 5 / 100)
print(f"O produto que custava {preco:.2f}, na promoção com desconto de 5% vai custar {precoDesconto:.2f}")
