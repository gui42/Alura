class Cliente:
    def __init__(self, cliente):
        self.__cliente = cliente

    @property
    def nome(self):
        print("Chamando propriedade nome()")
        return self.get_nome()

    def get_nome(self):
        return self.__cliente.title()

    @nome.setter
    def nome(self, nome):
        self.__cliente = nome
