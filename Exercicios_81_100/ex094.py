'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

lista = []
dicionario = {}
continuar = ""
media_idade = soma = 0

while True:
    dicionario["nome"] = input("Nome: ").strip()
    dicionario["sexo"] = input("Sexo [M/F]: ").strip().upper()
    while True:
        if dicionario["sexo"] not in "MF":
            print("ERRO! Por favor, digite apenas M ou F.")
            dicionario["sexo"] = input("Sexo [M/F]: ").strip().upper()
        else:
            break
    dicionario["idade"] = int(input("Idade: "))
    soma += dicionario["idade"]
    lista.append(dicionario.copy())
    continuar = input("Deseja continuar [S/N]: ").strip().upper()
    while True:
        if continuar not in "SN":
            print("ERRO! Responda apenas S ou N.")
            continuar = input("Deseja continuar [S/N]: ").strip().upper()
        elif continuar == "N":
            break
        elif continuar == "S":
            break
    if continuar == "S":
        continue
    else:
        break

print("=-=" * 15)

media_idade = soma / len(lista)

print(f"A) Ao todo temos {len(lista)} pessoas cadastradas.\n"
      f"B) A média de idade é de {media_idade} anos.\n"
      f"C) As mulheres cadastradas foram ", end="")

for p in lista:
    if p["sexo"] in "F":
        print(f"{p['nome']}", end=" ")
print()

print("D) Lista de pessoas que estão acima da média:")
for p in lista:
    if p["idade"] >= media_idade:
        print(f"  ")
        for k, v in p.items():
            print(f"{k} = {v}", end=" ")
        print()

print("<< ENCERRANDO >>")
