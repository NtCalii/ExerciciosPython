'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for.'''

n1 = int(input("Digite um número: "))
for c in range(1, 11):
    print(f"{c} X {n1} = {c * n1}")
