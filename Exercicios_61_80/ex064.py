'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag)'''

cont = soma = cont2 = 0
while cont != 999:
    cont = int(input("Digite um número [999 para parar]: "))
    if cont != 999:
        soma = soma + cont
        cont2 += 1
print(f"Você digitou {cont2} números, a soma entre todos eles é {soma}")
