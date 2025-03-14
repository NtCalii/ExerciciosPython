'''Faça um programa que leia duas notas e tire uma média, abaixo de 5.0 esta reprovado, entre 5,0 e
6,9 esta de recuperação e acima ou igual a 7,0 esta aprovado.'''

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
me = (n1 + n2) / 2
print(f"A média de {n1} mais {n2} é {me:.1f}")
if me >= 7:
    print("O aluno esta aprovado.")
elif me >= 5 and me <= 6.9:
    print("O aluno esta de recuperação.")
else:
    print("O aluno esta reprovado.")

#poderia ser elif 7 > me >=5
