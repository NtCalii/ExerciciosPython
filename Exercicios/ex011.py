#Faça um programa que leia a largura e altura de uma parede em metros, qualcule a área e a quantidade de
#tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m2.

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
tinta = area / 2
print(f"Sua parede têm a dimensão de {larg}x{alt} e sua área é de {area}m2.\n"
      f"Para pintar toda a parede, será necessário {tinta}l de tinta")
