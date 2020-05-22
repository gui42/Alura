class ContaCorrente:

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            raise LookupError("Saldo insuficente")

    def depositar(self, valor):
       self.saldo += valor

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __str__(self):
        return f">>Codigo: {self.codigo}\tSaldo: {self.saldo}<<"

    def __lt__(self, outro):
        return self.saldo < outro.saldo
       
    def __eq__(self, outro):
        return self.codigo == outro.codigo
