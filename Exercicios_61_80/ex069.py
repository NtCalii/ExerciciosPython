'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

idade = contIdade = contHomem = contMulher = 0
sexo = ""
continuar = "S"

print("-=-" * 10)
print("     CADASTRE UMA PESSOA")
print("-=-" * 10)

while continuar == "S":
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    print("-=-" * 10)
    if idade >= 18:
        contIdade += 1
    if sexo == "M":
        contHomem += 1
    if sexo == "F" and idade < 20:
        contMulher += 1
    continuar = input("Quer continuar [S/N]: ").strip().upper()

print(f"O total de pessoas com mais de 18 anos: {contIdade}\n"
      f"Ao todo temos {contHomem} homens cadastrados.\n"
      f"E temos {contMulher} mulher cadastrada com menos de 20 anos.")
