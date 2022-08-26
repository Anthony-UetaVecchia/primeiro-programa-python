import random


def jogar():
    print("**********************************")
    print("Bem vindo ao Jogo de Adivinhação")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):

        print("Digite um número de 1 a 100")
        print('tentativa {} de {}'.format(rodada, tentativas))

        chute_str = input("Digite o seu número: ")
        chute = int(chute_str)
        acertou = chute == numero_secreto
        errou_a_mais = chute > numero_secreto
        errou_a_menos = chute < numero_secreto

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100: ')
            continue

        if acertou:
            print("você acertou com {}".format(pontos))
            break
        else:
            if errou_a_mais:
                print('Você errou! O seu chute foi maior do que o número secreto')
            elif errou_a_menos:
                print('Você errou! O seu chute foi menor do que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Cabô')


if __name__ == '__main__':
    jogar()
