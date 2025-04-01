'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint

def somaPar(lista3):
    soma = 0
    for i in lista3:
        if i % 2 == 0:
            soma += i
    print(f"Somando os valores pares {lista3}, temos {soma}")

def sorteia(lista2):
    for cont in range(0, 6):
        lista2.append(randint(1, 20))
    print(f"Sorteando 5 valores: {lista2}", flush=True)
    somaPar(lista2[:])

lista = []
sorteia(lista[:])
