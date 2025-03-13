'''Escreva um programa que leia a velocidade de um veiculo, se ele passar de 80km/h ele vai ser
multado e vai ter que pagar R$7,00 por km a mais do límite.'''

km = int(input("Qual a velocidade atual do veículo: "))
if km < 80:
    print("Tenha um bom dia, dirija com segurança!")
else:
    multa = (km - 80) * 7
    print("MULTADO! Você excedeu o limite permitido de 80Km/h\n"
          f"Você deve pagar uma multa de {multa:.2f}")
