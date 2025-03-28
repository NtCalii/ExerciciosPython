'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação, salário e idade.'''

pessoa = {}
pessoa["nome"] = input("Nome: ")
pessoa["nascimento"] = int(input("Ano de nascimento: "))
pessoa["carteira"] = int(input("Carteira de Trabalho (0 não tem): "))
if pessoa["carteira"] != 0:
    pessoa["contratação"] = int(input("Ano de contratação: "))
    pessoa["salario"] = float(input("Sálario: R$"))
print("=-=" * 15)
print(f"- Nome é igual a {pessoa['nome']}\n"
      f"- Idade é igual a {2025 - pessoa['nascimento']}\n"
      f"- CTPS é igual a {pessoa["carteira"]}")
if pessoa["carteira"] != 0:
    print(f"- Contrtação feita em {pessoa['contratação']}\n"
          f"- Sálario igual a R${pessoa['salario']}")
