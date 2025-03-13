'''Faça um programa que pergunte a ditância de uma viagem e calcule o preço da passagem, cobrando R$0,50
por km para viagens de até 200km, para viagens mais longas o preço é de R$0,45 por km.'''

km = int(input("Qual a distância em Km da viagem a ser feita? "))
if km <= 200:
    print(f"O valor de sua passagem é de R${km * 0.5}")
else:
    print(f"O valor de sua passagem é de R${km * 0.45}")
