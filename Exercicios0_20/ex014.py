#Escreva um programa que converta uma temperatura digitada em C para F.

tC = float(input("Informe a temperatura em C: "))
tF = tC * 1.8 + 32
print(f"A temperatura em {tC:.1f}C corresponde a {tF:.1f}F!")
