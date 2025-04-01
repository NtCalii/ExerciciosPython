'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*num):
    print("=-=" * 20)
    print(f"Analizando os valores passados...\n"
          f"{num} foram informados {len(num)} valores ao todo.\n"
          f"O maior valor foi {max(num)}.")
    print("=-=" * 20)

maior(5,34,2,78,43,53,7,63,4)
