class MinhaClasse:
    estatico = "Ola mundo"

    def __init__(self, estado) -> None:
        self.estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = "Progrmador"
obj1.estatico = "Lhama"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
