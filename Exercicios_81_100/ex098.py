'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada.'''

from time import sleep

def contador(ini, fi, pas):
    if pas == 0:
        pas = 1
    abs(pas)
    print(f"Contagem de {ini} até {fi} contando de {pas} em {pas}")
    cont = ini
    if cont < fi:
        while cont <= fi:
            print(f"{cont}",end=" ")
            sleep(0.5)
            cont += pas
        print("FIM!")
        print("=-=" * 20)
    else:
        while cont >= fi:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont -= pas
        print("FIM!")
        print("=-=" * 20)

inicio = fim = passo =0

print("=-=" * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!!!")
inicio = int(input("Ínicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
