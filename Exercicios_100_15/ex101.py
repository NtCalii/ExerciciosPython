'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade >= 18:
        return print(f"Com {idade} anos: VOTO OBRIGATÓRIO!")
    elif 16 <= idade < 18 or idade >= 65:
        return print(f"Com {idade} anos: VOTO OPCIONAL!")
    else:
        return print(f"Com {idade} anos: VOTO NEGADO!")

nasc = int(input("Em  que ano você nasceu? "))
print(voto(nasc))
