import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu Jogo!*******")
    print("*********************************")

    print('(1)Forca (2)Adivinhação')

    jogo = int(input('Qual jogo? '))

    if (jogo == 1):
        print('Jogando Forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando Adivinhação')
        adivinhacao.jogar()
    else:
        if not (jogo == 1 or jogo == 2):
            print('Escolha um número válido')

if (__name__ == '__main__'):
    escolhe_jogo()
