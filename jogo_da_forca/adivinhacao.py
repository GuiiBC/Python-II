from random import randint
from time import sleep

def jogar():
    print("-" * 19)
    print("JOGO DA ADIVINHAÇÃO")
    print("-" * 19)

    numero_secreto = randint(1, 10)
    rodadas = 0
    tentativas = 1
    pontos = 100

    print("1)Fácil  2)Normal  3)Difícil")

    dificuldade = int(input("Digite a dificuldade: "))

    if dificuldade == 1:
        rodadas = 6

    elif dificuldade == 2:
        rodadas = 3

    else:
        rodadas = 1

    while tentativas <= rodadas:
        print(f"Tentativa {tentativas} de {rodadas}:")
        chute = int(input("Digite o seu chute entre 1 e 10: "))

        if chute < 1 or chute > 10:
            print("Digite um número válido")
            continue

        if numero_secreto == chute:
            print(f"Você acertou e fez {pontos} pontos.")
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontosPerdidos = abs(numero_secreto - chute)
            pontos = pontos - pontosPerdidos
            print(f"Você perdeu {pontosPerdidos} pontos. Você possui {pontos} pontos agora.")

        tentativas = tentativas + 1

    print("O número era", numero_secreto)
    print("Fim de jogo.")


if __name__ == '__main__':
    while True:
        jogar()
        restart = int(input("Deseja jogar novamente? 0)Sim  1)Não: "))
        if restart == 0:
            continue
        elif restart == 1:
            print("Obrigado por jogar")
            sleep(2)
            break
