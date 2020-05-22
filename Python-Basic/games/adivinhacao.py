import random


def jogar():

    vitoria = False
    numero_secreto = random.randrange(1, 101)
    pontuacao = 1000
    mensagem()
    total_tentativas = escolhe_dificuldade()

    for tentativa_atual in range(1, total_tentativas+1):
        print("\nTentativa {} de {}".format(tentativa_atual, total_tentativas))
        chute = int(input("Entre com um numero: "))
        chute_menor = chute < 1
        chute_maior = chute > 100

        if chute_menor or chute_maior:
            print("Numero fora do intervalo!")
            continue

        maior_que_numero = chute > numero_secreto
        menor_que_numero = chute < numero_secreto
        vitoria = chute == numero_secreto

        if vitoria:
            print("VOCÊ GANHOU!\nSua pontuação foi de: {:0004d}!!".format(pontuacao))
            break
        else:
            if menor_que_numero:
                print("O numero é maior!")
            elif maior_que_numero:
                print("O numero é menor!")
                pontuacao = pontuacao - (abs(numero_secreto - chute))

    print("fim do jogo!")
    if not vitoria:
        print("\nO numero era {}\nSua Pontuação foi de: {:0004d}".format(numero_secreto, pontuacao))


def escolhe_dificuldade():
    dificuldade = [15, 10, 5]
    for x in range(0, len(dificuldade)):
        print("({}) - {} Tentativas".format(x, dificuldade[x]))

    while True:
        escolha = input("Escolha uma dificuldade: ")
        if escolha.isdecimal():
            escolha = int(escolha)
            if escolha < len(dificuldade):
                return dificuldade[escolha]

        print("Escolha invalida!")


def mensagem():
    print("------------------------------------", "Tente adivinhar o numero!", "As entradas devem ser entre 1 e 100", "------------------------------------", sep="\n")


if __name__ == "__main__":
    jogar()