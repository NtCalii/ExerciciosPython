class Minha_Classe:
    def __init__(self, info, elem):
        self.atributo_1 = "Meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "oi"]
        self.atributo_novo = info
        print(self.atributo_novo)

    def metodo_1(self):
        print("Minha ação 1")
        print("Minha ação 2")
        print(self.atributo_2)
        return "Olá Mundo"

    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)

minha_classe = Minha_Classe("info aqui no construtor", 213)

minha_classe.metodo_2(3)
