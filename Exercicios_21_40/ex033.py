'''Faça um programa que leia 3 números e fala qual é o menor e maior entre eles.'''

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))
lista = [n1, n2, n3]
print(f"O maior número é {max(lista)}")
print(f"O menor número é {min(lista)}")
