'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.'''

n1 = cont = soma = maior = menor =0
resp = ""
while resp not in ["N", "n"]:
    n1 = int(input("Digite um valor: "))
    cont += 1
    soma = soma + n1
    if cont == 1:
        maior = menor = n1
    else:
        if maior < n1:
            maior = n1
        if menor > n1:
            menor = n1
    resp = input("Quer continuar [S/N]: ")
print(f"Você digitou {cont} números e a média entre eles foi {soma / cont:.2f}\n"
      f"O maior valor foi {maior} e o menor valor foi {menor}")
