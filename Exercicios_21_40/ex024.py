'''Crie um programa que leia o nome de uma cidade e diga se ela começa com "Santo".'''

city = input("Qual o nome da cidade: ").strip()
nome = city.capitalize()
print(f"{"Santo" in nome}")
