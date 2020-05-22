import random


def jogar():
    mensagem()
    palavra_secreta = escolhe_palavra()

    erros = 0
    enforcou = False
    acertou = False
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    total_tentativas = escolhe_dificuldade()

    while not enforcou and not acertou:
        desenha_forca(erros)
        imprimir_palavra(letras_acertadas)

        print("Total de Letras: {}\t Total de tentativas restando: {:2d}".format(len(palavra_secreta), (total_tentativas-erros)))

        chute = pede_chute()

        if chute in palavra_secreta:
            letras_acertadas = atualiza_letras_acertadas(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print("Ops, voce errou")

        enforcou = erros == total_tentativas
        acertou = "_" not in letras_acertadas

    mensagem_final(acertou, palavra_secreta)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if (erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros >= 7 ):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem():
    print("-------------------------------", "Bem Vindo ao jogo de Forca!", "-------------------------------", sep="\n")


def imprimir_palavra(lista):
    for x in range(0, len(lista)):
        print(lista[x], end="")
    print()


def escolhe_palavra():
    with open("palavras.txt") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip().upper())

    palavra_secreta = palavras[random.randrange(1, len(palavras))]
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for x in palavra]
    return letras_acertadas


def escolhe_dificuldade():
    dificuldade = [20, 15, 10, 5]
    dificuldade.sort()
    dificuldade.reverse()
    print("Niveis:")
    while True:
        for x in range(0, len(dificuldade)):
                print("({:1d}) - {:02d} Tentativas".format(x, dificuldade[x]))

        escolha = input("Escolha uma dificuldade: ")
        if escolha.isdecimal():
            escolha = int(escolha)
            if escolha < len(dificuldade):
                return dificuldade[escolha]

        print("Opção invalida")


def pede_chute():
    while True:
        chute = input("Escolha uma letra:")
        if chute.isalpha():
            return chute.strip().upper()
        print("Entrada invalida!")


def atualiza_letras_acertadas(chute, palavra, lista):
    for x in range(0, len(palavra)):
        if chute == palavra[x]:
            lista[x] = chute
    return lista


def mensagem_final(vitoria, palavra):
    if vitoria:
        print("Você ganhou! Parabens!")
    else:
        print("A palavra era '{}'!\nMais sorte na proxima vez!".format(palavra))


if __name__ == "__main__":
    jogar()
