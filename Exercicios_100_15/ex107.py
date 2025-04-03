'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
 e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

preco = float(input("Digite um preço: R$"))
print(f"A metade desse preço é R${moeda.metade(preco):.2f}")
print(f"O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}")
print(f"Aumentando 10% fica R${moeda.aumentar(preco):.2f}")
