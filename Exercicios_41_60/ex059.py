''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
op = 0
while op != 5:
    print("[1] somar\n"
          "[2] subtrair\n"
          "[3] multiplicar\n"
          "[4] dividir\n"
          "[5] sair do programa")

    op = int(input("Qual a sua escolha: "))

    match op:
        case 1:
            print(f"A soma de {n1} + {n2} é {n1 + n2}")
        case 2:
            print(f"A subtração de {n1} - {n2} é {n1 - n2}")
        case 3:
            print(f"A multiplicação de {n1} X {n2} é {n1 * n2}")
        case 4:
            print(f"A divisão de {n1} / {n2} é {n1 / n2:.2f}")
        case 5:
            print("Fim do programa.")
        case _:
            print("Erro, tente novamente")
    print("-=-" * 10)
