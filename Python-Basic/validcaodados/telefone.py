import re
class Telefone:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("numero incorreto")

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def formata_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        if resposta.group(1):
            return "+{}({}){}-{}".format(
                resposta.group(1),
                resposta.group(2),
                resposta.group(3),
                resposta.group(4)
                )
        else:
            return "({}){}-{}".format(
                resposta.group(2),
                resposta.group(3),
                resposta.group(4)
                )

    def __str__(self):
        return self.formata_numero()
