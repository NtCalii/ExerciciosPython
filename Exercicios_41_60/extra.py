'''Treinar o match case.'''

print("-=-" * 10)
print("   DOAÇÃO CRIANÇA ESPERANÇA")
print("-=-" * 10)
print("Valores de doação.\n"
      "[1] para R$20\n"
      "[2] para R$60\n"
      "[3] para R$110")
n1 = int(input("Qual o valor que você deseja doar: "))
match n1:
    case 1:
        print("PARABÉNS!!! você fez uma doação no valor de R$20")
    case 2:
        print("PARABÉNS!!! você fez uma doação no valor de R$60")
    case 3:
        print("PARABÉNS!!! você fez uma doação no valor de R$110")
    case _:
        print("ERRO!!! Valor invalido")
