'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

escola = {}
escola["nome"] = input("Nome: ")
escola["nota"] = int(input("Nota: "))
print("=-=" * 10)
print(f"- Nome é igual a {escola['nome']}\n"
      f"- Nota é igual a {escola['nota']}\n"
      f"- Situação é igual a ", end="")
if escola["nota"] >= 7:
    print("APROVADO.")
elif escola["nota"] >= 5:
    print("RECUPERAÇÃO.")
else:
    print("REPROVADO.")
