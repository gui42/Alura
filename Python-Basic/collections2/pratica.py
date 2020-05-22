#testando o uso de diversas colecoes

from collections import Counter

texto1 = """
Para entender o Kubernetes e o que ele é, vamos começar falando brevemente de Docker. O Docker é a ferramenta padrão para deployar/implementar uma aplicação usando containers. Em outras palavras, o Docker se baseia no formato mais popular para empacotar uma aplicação e é a container engine mais usada.
"""
texto2 = """
Ainda em beta, lançamos o caderno, nova função da Alura que permite o registro de suas anotações dentro da própria plataforma enquanto assiste aos nossos cursos.
"""
def analisa_frequencia(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values())
    proporcao = [(letra, frequencia/total_caracteres) for letra, frequencia in aparicoes.items()]
    proporcao = Counter(dict(proporcao))
    for caractere, pro in proporcao.most_common(5):
        print("\t{}:{:.02f}%".format(caractere, pro*100))

print("texto 1:")
analisa_frequencia(texto1)
print("texto 2:")
analisa_frequencia(texto2)
