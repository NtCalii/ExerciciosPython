'''Crie um programa que vai gerar quatro números aleatórios e colocar em uma tupla. Depois disso, mostre
a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os valores sorteados foram {valores}")
print(f"O valor mais alto foi {max(valores)}")
print(f"O valor mais baixo foi {min(valores)}")
