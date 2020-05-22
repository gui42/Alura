

class Conta:

    def __init__(self, numero, titular, saldo = 0.0, limite = 1000.0):
        print("Construindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def get_codigo_banco():
        return "001"

    def get_titular(self):
        return self.__titular

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print("Saldo: {:.02f} do titular {}".format(self.__saldo, self.__titular.capitalize()))

    def __pode_sacar(self, quantidade):
        limite_total = self.__saldo + self.__limite
        if quantidade >= limite_total:
            return True
        else:
            return False

    def sacar(self, quantidade):
        if self.__pode_sacar:
            self.__saldo -= quantidade
        else:
            print("Limite estorado! o.o")

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)
