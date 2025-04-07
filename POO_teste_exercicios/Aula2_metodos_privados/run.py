class Pessoa:
    def __init__(self, altura, cpf):
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f"Olá! Minha altura - {self.altura}")
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f"Meu documento - {self.__cpf}")

jorge = Pessoa("1.70", "874.358.973-29")
jorge.apresentar()
