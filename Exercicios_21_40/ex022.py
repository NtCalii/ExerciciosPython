'''Crie um programa que leia um nome completo de uma pessoa e mostre na tela o nome todo em maiúsculo
e também todo em minúsculo, quantas letras ao total (sem os espaços), o primeiro nome e quantas letras
tem nele ao total.'''

nome = (input("Digite seu nome completo: ")).strip()
print(f"Analisando seu nome...\n"
      f"Seu nome em maiúsculo é: {nome.upper()}\n"
      f"Seu nome em minúscula é: {nome.lower()}\n"
      f"Seu nome tem ao todo: {len(nome) - nome.count(" ")} letras\n"
      f"Seu primeiro nome é: {nome.split()[0]} e ele tem {len(nome.split()[0])} letras")
