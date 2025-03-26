'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta.'''

from random import randint
n1 = num = cont1 = cont2 = 0
jogo = []
lista = []
print("=-=" * 10)
print("      JOGO DA MEGA SENA")
print("=-=" * 10)
n1 = int(input("Quantos jogos você quer que eu sorteie: "))
print(f"=-=-= SORTEANDO {n1} JOGOS =-=-=")
for cont1 in range(1, n1 + 1):
    cont2 = 0
    while True:
        num = randint(0, 60)
        if num not in jogo:
            jogo.append(num)
            cont2 += 1
        if cont2 == 6:
            break
    lista.append(jogo[:])
    jogo.clear()
    print(f"Jogo {cont1}: {lista[cont1 - 1]}")
print("=-=" * 3, "BOA SORTE", "=-=" * 3)
