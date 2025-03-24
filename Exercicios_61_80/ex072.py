'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.'''

numero = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")
n1 = int(input("Digite um número entre 0 e 10: "))
if 0 <= n1 < 11:
    print(numero[n1])
else:
    print("O número não esta entre 0 e 10.")
