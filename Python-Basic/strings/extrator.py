class Extrator:
    def __init__(self, url):
        if self.valida_url(url):
            self.url = url



    def retorna_moeda_destino(self):
        moeda = "moedadestino"
        index = self.url.find(moeda) + len(moeda)+1
        url2 = self.url.replace("&", "", 1)
        fim_moeda = url2.find("&") + 1
        moeda_destino = self.url[index:fim_moeda]
        return moeda_destino

    def retorna_moeda_origem(self):
        moeda = "moedaorigem"
        index = self.url.find(moeda) + len(moeda)+1
        fim_moeda = self.url.find("&")
        moeda_origem = self.url[index:fim_moeda]
        return moeda_origem

    @staticmethod
    def valida_url(url):
        if url:
            return True
        else:
            raise LookupError("url invalida")

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)+1
