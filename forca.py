import random




def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta('palavra.txt')

    letras_acertadas = inicializa_letra_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7
    
    seletor_de_palavras()

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print('Não existe essa letra na palavra!')
            print('Você possui {} tentativas'.format(tentativas - erros))

        enforcou = erros == tentativas
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao Jogo de Forca!***")
    print("*********************************")

def carrega_palavra_secreta(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letra_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Escolha uma letra: ')
    chute = chute.strip().upper()
    return chute

def seletor_de_palavras():
    arquivo = open('palavra.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letter in palavra_secreta:
        if (chute == letter):
            letras_acertadas[index] = letter
        index = index + 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_ganhador():
    print('Párabens! Você descobriu a palavra secreta!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('Cabô')


def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {},".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print('cabô')

if (__name__ == '__main__'):
    jogar()