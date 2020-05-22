meu_texto = "the quick brown fox jumps over the lazy dog"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agr = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agr + 1

print(aparicoes)
