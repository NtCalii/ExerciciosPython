'''Crie uma tupla preenchida com os 8 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 4 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Bragantino.'''

times = ("São Paulo", "Bragantino", "Vasco", "Palmeiras", "Corinthians", "Flamengo", "Barcelona", "Cruzeiro")
print("-=-" * 20)
print(f"Lista dos times brasileiros {times}")
print("-=-" * 20)
print(f"Os 4 primeiros são {times[0:4]}")
print("-=-" * 20)
print(f"Os 4 últimos são {times[4:]}")
print("-=-" * 20)
print(f"Em ordem alfabética {sorted(times)}")
print("-=-" * 20)
print(f"O Brangantino está na posição {times.count("Bragantino") + 1}")
print("-=-" * 20)
