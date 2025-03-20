'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''

n1 = cont =0
while True:
    n1 = int(input("Quer ver qual tabuada: "))
    print("-=-" * 10)
    if n1 < 0:
        break
    for cont in range(1, 11):
        print(f"{n1} X {cont} = {n1 * cont}")
    print("-=-" * 10)
print("FIM.")
