class MinhaClasse:
    estatico = "Ola mundo"

    def __init__(self, estado) -> None:
        self.estado = estado

    def print_variavel_de_classe(self):
        print(self.estatico)

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

obj1.print_variavel_de_classe()
