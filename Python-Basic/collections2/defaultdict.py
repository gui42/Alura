from collections import defaultdict, Counter 
aparicoes = defaultdict(int)  #defaultdict aceita uma função como parametro e aplica essa função por default para o valor de chaves novas

meu_texto = "The quick brown fox jumped over the lazy dog"

for palavra in meu_texto.split():
    aparicoes[palavra] += 1 

for chave, valor in aparicoes.items():
    print(chave,":",valor)

print()

outro = Counter(meu_texto.split())

print(outro)
