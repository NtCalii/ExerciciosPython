'''Faça o programa que leia o ano de nascimento de uma pessoa e informe se ela já se alistou e
quanto tem foi isso, se ela ainda precisa se alistar e quando vai ser, e se ela precisa se alistar
este ano. Levando em conta que precisa se alistar com 18 anos.'''

from datetime import date

nascimento = int(input("Qual o seu ano de nascimento: "))
idade = date.today().year - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {date.today().year}")
if idade > 18:
    n1 = idade - 18
    print(f"Você já deve ter se alistado há {n1} anos.\n"
          f"Seu alistamento foi em {date.today().year - n1}.")
elif idade < 18:
    n1 = 18 - idade
    print(f"Ainda faltam {n1} anos para o alistamento.\n"
          f"Seu alistamento será em {date.today().year + n1}.")
else:
    print(f"Você precisa se alistar este ano.")
