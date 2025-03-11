#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informaçoes
#possivesi sobre ela.

algo = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(algo),
      "Só tem espaços? ", algo.isspace(),
      "É um número? ", algo.isnumeric(),
      "É alfabético? ", algo.isalpha())
