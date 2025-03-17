'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

media = 0
idadeHomem = 0
nomeHomem = ""
mulheres = 0

for c in range(1, 5):
    print(f"----- {c} PESSOA -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("[M]/[F]: ").strip()
    media = media + idade
    if sexo == "M" or "m":
        if idade > idadeHomem:
            idadeHomem = idade
            nomeHomem = nome
    if sexo == "F" or "f" and idade < 20:
        mulheres += 1

print(f"A média de idade do grupo é de {media/4:.1f} anos.\n"
      f"O homem mais velho tem {idadeHomem} e se chama {nomeHomem}.\n"
      f"Ao todo tem {mulheres} com menos de 20 anos.")
