'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaReal() com a
mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            num_int = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"ERRO: Por favor, digite um número inteiro válido.")
            continue
        else:
            break
    return num_int

def leiaReal(msg):
    while True:
        try:
            num_real = float(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"ERRO: Por favor, digite um número real válido.")
            continue
        else:
            break
    return num_real

num_int = leiaInt("Digite uma valor inteiro: ")
num_real = leiaReal("Digite um real: ")
print(f"O valor inteiro digitado foi {num_int} e o real foi {num_real}")
