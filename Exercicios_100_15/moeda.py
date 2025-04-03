'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), dobro()
 e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

def aumentar(n1):
    n1 = n1 * 10 / 100
    return n1

def dobro(n1):
    n1 *= 2
    return n1

def metade(n1):
    n1 /= 2
    return n1
