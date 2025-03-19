'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só
que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.'''

from random import randint

computador = randint(0, 10)
jogador = 11
tentativa = 0
print("Sou seu computador...\n"
      "Acabei de pensar em um número de 0 até 10.\n"
      "Será que você consegue adivinhar qual foi?")

jogador = int(input("Qual o seu palpite: "))

while jogador != computador:
    if jogador > computador:
        print("Quase... mais baixo.")
    elif jogador < computador:
        print("Quase... mais alto.")
    print("Você errou, tente de novo.")
    jogador = int(input("Qual o seu palpite: "))
    tentativa += 1
print(f"Você acertou em {tentativa} tentativas. Parabéns!")
