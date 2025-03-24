'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

núm = (int(input("Digite um número: ")), int(input("Digite um número: ")),
       int(input("Digite um número: ")), int(input("Digite um número: ")))
print(f"Você digitou os valores {núm}")
print(f"O valor nove apareceu {núm.count(9)} vezes")
if 3 in núm:
    print(f"O valor 3 apareceu na posição {núm.index(3) + 1}")
else:
    print("Não existe o valor 3")
print("Os valores pares foram: ", end="")
for c in núm:
    if c % 2 == 0:
        print(c, end=" ")
