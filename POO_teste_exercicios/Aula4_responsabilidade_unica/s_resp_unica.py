class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__erro_handler()

    def __validate_input(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)

    def __register_user(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados...")
        print(f"Cadastrar usuario {nome}, idade {idade}")

    def __erro_handler(self) -> None:
        print("Dados invalidos")

sistema = SistemaCadastral()
sistema.cadastrar("Nathan", 19)
