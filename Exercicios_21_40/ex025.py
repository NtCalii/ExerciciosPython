'''Crie um programa que leia o nome completo de uma pessoa e diga se ela tem "Silva" no nome.'''

nome = input("Qual o seu nome completo: ").strip()
nomeNor = nome.title()
print(f"Seu nome tem Silva? {"Silva" in nomeNor}")
