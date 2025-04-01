'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''

def area(l, c):
    a = l * c
    print(f"A área de {l} X {c} é de {a}m2.")

print("Controle de Terrenos")
print("=-=" * 10)
l = float(input("Digite a largura (m): "))
c = float(input("Digite o comprimento (m)"))
area(l, c)
