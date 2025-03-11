#Um professor quer sortear um dos quatro alunos. Faça um programa que ajude ele, lendo o nome deles e
#escrevendo o nome do escolhido.

from random import choice

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
print(f"O aluno escolhido foi {choice([aluno1, aluno2, aluno3, aluno4])}")
