#Escreva um programa que leia um valor em metros e o exiba convertidos em centrímetros e milímetros.

medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
print(f"A medida de {medida}m corresponde a {cm}cm e {mm}mm")
