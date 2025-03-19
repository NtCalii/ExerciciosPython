'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja
errado, peça a digitação novamente até ter um valor correto.'''

sexo = ""
sexo = input("Digite seu sexo [M/F]: ").upper().strip()[0]
while sexo not in "MF":
        sexo = input("Dados inválidos. Por favor, informe seu sexo [M/F]: ").upper().strip()[0]
print(f"Sexo {sexo} foi registrado com sucesso.")
