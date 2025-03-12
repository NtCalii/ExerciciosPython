'''Faça um programa que leia uma frase e mostre quantas letra "a" tem e a primeira posição que ela
aparece e a última também, começando a contagem do 1.'''

frase1 = input("Digite uma frase: ").strip()
frase2 = frase1.lower()
print(f"A letra A aparece {frase2.count("a")} vezes na frase.\n"
      f"A primeira letra A apareceu na posição {frase2.find("a")+1}.\n"
      f"A última letra A apareceu na posição {frase2.rfind("a")+1}.")
