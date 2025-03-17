'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores, levando em conta 21 maior de idade.'''

#eu não quis importa o datetime

maior = 0
menor = 0
for c in range(1, 8):
    n1 = int(input(f"Em que ano a {c} pessoa nasceu: "))
    if 2025 - n1 >= 21:
        maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade.\n"
      f"E {menor} pessoas menores de idade.")
