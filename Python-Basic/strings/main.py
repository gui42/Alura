from extrator import Extrator

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
url2 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dólar"
extrator = Extrator(url)

print(extrator.retorna_moeda_origem())
print(extrator.retorna_moeda_destino())