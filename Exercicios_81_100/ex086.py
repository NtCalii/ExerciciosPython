'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[], [], []], [[], [], []], [[], [], []]
contColuna = contLinha = 0
for coluna in matriz:
    for linha in coluna:
        linha.append(int(input(f"Digite o valor para [{contColuna}, {contLinha}]: ")))
        contLinha += 1
    contColuna += 1
    contLinha = 0
print("=-=" * 15)
print(f"{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}\n"
      f"{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}\n"
      f"{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}")
