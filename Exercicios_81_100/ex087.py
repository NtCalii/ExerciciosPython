'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valorPar = valorColuna = valorLinha = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite o valor para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            valorPar += matriz[linha][coluna]
for linha in range(3):
    valorColuna += matriz[linha][2]
valorLinha = max(matriz[1])
print("=-=" * 15)
for linha in matriz:
    print(*linha)
print("=-=" * 15)
print(f"A soma dos valores pares é {valorPar}")
print(f"A soma dos valores da terceira coluna é {valorColuna}")
print(f"O maior valor da segunda linha é {valorLinha}")
