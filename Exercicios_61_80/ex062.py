'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerrará quando ele disser que quer mostrar 0 termos.'''

print("=" * 20)
print("GERADOR DE PA")
print("=" * 20)
termo = int(input("Primeiro termo: "))
razão =  int(input("Razão: "))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razão
        cont += 1
    print("PAUSA.")
    mais = int(input("Quantos termos você quer mostrar a mais: "))
print(f"Progressão finalizada com {total} termos mostrados.")
print("FIM.")
