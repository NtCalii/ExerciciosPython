#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
#dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e
#R$0,15 por Km rodado.

dias = int(input("Quantos dias o carro foi alugado: "))
kilometros = float(input("Quantos Km foi rodado com o carro: "))
preco = (dias * 60) + (kilometros * 0.15)
print(f"O total a pagar é de {preco}")
