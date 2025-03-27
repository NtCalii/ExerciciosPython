'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''

lDefi = []
lProv = []
while True:
    nome = continuar= ""
    nota1 = nota2 = 0
    nome = input("Nome: ")
    lProv.append(nome)
    nota1 = float(input("Nota 1: "))
    lProv.append(nota1)
    nota2 = float(input("Nota 2: "))
    lProv.append(nota2)
    lDefi.append(lProv[:])
    lProv.clear()
    continuar = input("Quer continuar [S/N]: ").upper()
    if continuar == "N":
        break
print("=-=" * 15)
print(f"No.  NOME          MÉDIA\n"
      f"------------------------")
for c, n in enumerate(lDefi):
    print(f"{c}   {lDefi[c][0]}         {(lDefi[c][1] + lDefi[c][1]) / 2}")
print("=-=" * 15)
while True:
    interrompe = 0
    interrompe = int(input("Mostrar nota de qual aluno? (999 finaliza): "))
    if interrompe == 999:
        break
    print(f"Notas de {lDefi[interrompe]}")
    print("=-=" * 15)
