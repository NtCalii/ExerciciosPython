'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), dobro()
 e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

def aumentar(n1, taxa=0):
    n1 = n1 * taxa / 100
    return n1

def dobro(n1):
    n1 *= 2
    return n1

def metade(n1):
    n1 /= 2
    return n1

#def moedas(preco=0):
#    return f"{moedas()}{preco:>8.2f}".replace(".", ",")

def resumo(n1, taxa):
    print("---------------\n"
          "RESUMO DO VALOR\n"
          "---------------")
    print(f"Preço analisado: {n1}\n"
          f"Dobro do preço: {dobro(n1)}\n"
          f"Metade do preço: {metade(n1)}\n"
          f"{taxa}% de aumento: {aumentar(n1, taxa)}")
