import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP invalido")
    
    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
                dados['bairro'],
                dados['localidade'],
                dados['uf'],
                dados['logradouro']
                )

    def formata_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def __str__(self):
        return self.formata_cep()

    @staticmethod
    def cep_valido(cep):
        if len(cep) == 8:
            return True
        else:
            return False
