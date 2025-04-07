class Minha_classe:
    def __init__(self):
        self.__valor = None

    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    @property
    def getter_valor(self) -> int:
        return self.__valor

my_class = Minha_classe()
my_class.setter_valor(23)
print(my_class.getter_valor)
