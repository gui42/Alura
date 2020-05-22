import adivinhacao
import forca


def escolhe_jogo():
    continua = True

    while continua:
        print("(1) - Forca (2) - Adivinhacao - (3) - Sair")
        escolha = int(input("Escolha um jogo: "))

        if escolha == 1:
            print("Jogando Forca...")
            forca.jogar()
        elif escolha == 2:
            print("Jogando Adivinhacao...")
            adivinhacao.jogar()
        elif escolha == 3:
            continua = False


if __name__ == "__main__":
    escolhe_jogo()

