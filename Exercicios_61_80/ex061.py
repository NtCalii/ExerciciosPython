'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.'''

print("=" * 20)
print("GERADOR DE PA")
print("=" * 20)
termo = int(input("Primeiro termo: "))
razão =  int(input("Razão: "))
cont = 1
while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razão
    cont += 1
print("FIM.")
