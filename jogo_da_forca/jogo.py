import forca
import adivinhacao

def escolhe_jogo():
    print("-" * 16)
    print("ESCOLHA SEU JOGO")
    print("-" * 16)

    print("1)Forca")
    print("2)Adivinhação")

    jogo = int(input("Qual jogo: "))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()

if __name__ == '__main__':
    escolhe_jogo()