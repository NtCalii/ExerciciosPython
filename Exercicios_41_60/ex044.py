'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''

print("===== LOJAS CALI =====")
preço = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO\n"
      "[1] à vista no dinheiro\n"
      "[2] à vista no cartão\n"
      "[3] 2x no cartão\n"
      "[4] 3x ou mais no cartão")
op = int(input("Qual opção: "))
if op == 1:
    desconto = preço * 10 / 100
    print(f"Sua compra de R${preço} vai custar R${preço - desconto} no final da compra.")
elif op == 2:
    desconto = preço * 5 / 100
    print(f"Sua compra de R${preço} vai custar R${preço - desconto} no final no final da compra.")
elif op == 3:
    print(f"Sua compra vai custar R${preço} no final da compra")
elif op == 4:
    juros = preço * 20 / 100
    print(f"Sua compra de R${preço} vai custar R${preço + juros} no final no final da compra.")
else:
    print("Opção inválida.")
