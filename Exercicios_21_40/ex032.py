'''Faça um programa que leia um ano e fale se ele é BISSEXTO.'''

from datetime import date

ano = int(input("Qual ano analisar? Coloque 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é BISSEXTO")
else:
    print(f"O ano de {ano} não é um ano BISSEXTO")
