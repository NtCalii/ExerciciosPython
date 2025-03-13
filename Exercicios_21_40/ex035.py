'''Faça um programa que leia o tamanho de 3 linhas e fale se da para formar um triângulo.'''

print("-=" * 20)
print("Analisador de Triângulos")
print("-=" * 20)
n1 = int(input("Primeiro seguimento: "))
n2 = int(input("Segundo seguimento: "))
n3 = int(input("Terceiro seguimento: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os segmentos a cima formar um triângulo")
else:
    print("Não formamr um triângulo")
