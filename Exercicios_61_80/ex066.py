'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre elas (desconsiderando o flag).'''

n1 = cont = soma = 0
while True:
    n1 = int(input("Digite um valor [999 para parar]: "))
    if n1 == 999:
        break
    soma = soma + n1
    cont += 1
print(f"A soma dos {cont} valores é {soma}")
