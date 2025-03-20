'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint

soma = cont = 0
print("-=-" * 10)
print("   VAMOS JOGAR PAR OU ÍMPAR")
print("-=-" * 10)
while True:
    computador = randint(1, 10)
    jogadorNumero = int(input("Digite um valor: "))
    jogadorLetra = input("Par ou Ímpar [P/I]: ").strip().upper()
    soma = jogadorNumero + computador
    print("-=-" * 10)
    print(f"Você jogou {jogadorNumero} e o computador {computador}. Total de {soma} deu ", end="")
    print("PAR" if soma % 2 == 0 else "ÍMPAR")
    print("-=-" * 10)
    if jogadorLetra == "P":
        if soma % 2 == 0:
            print("Você GANHOU, Parabéns!!!")
            print("-=-" * 10)
            cont += 1
        else:
            print("Você PERDEU, Que pena.")
            print("-=-" * 10)
            break
    elif jogadorLetra == "I":
        if soma % 2 == 1:
            print("Você GANHOU, Parabéns!!!")
            print("-=-" * 10)
            cont += 1
        else:
            print("Você PERDEU, Que pena.")
            print("-=-" * 10)
            break
print(f"GAME OVER, você venceu {cont} vezes.")
