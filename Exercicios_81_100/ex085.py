'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.'''

par = []
impar = []
for cont in range(1, 8):
    n1 = int(input("Digite um valor: "))
    if n1 % 2 == 0:
        par.append(n1)
    else:
        impar.append(n1)
print("=-=" * 10)
par.sort()
impar.sort()
print(f"Os valores pares digitados foram {par}\n"
      f"Os valores ímpares digitados foram {impar}")
