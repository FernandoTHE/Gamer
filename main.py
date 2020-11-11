from random import randint


def main():
    while True:
        op = "0"
        op = str(input("1 - jogar\n2 - sair\n---> "))

        if op == "1":
            novo_jogo()
        if op == "2":
            break


def novo_jogo():

    ## vetor de objetos a serem colocados no mapa
    ## c = canion | d = mina diamantes | e = elefante
    objectsmap = ("C", "C", "C", "D", "E", "E", "E")

    ## preenchimento do mapa de 25 elementos (5x5)
    mapline = []
    for j in range(25):
        mapline.append(str(" "))

    ## alocação dos elementos no mapa
    for elemento in objectsmap:
        mapline[randint(0, 19)] = elemento

        ## organização do mapa em uma matriz:
    mapmatriz = []
    for i in range(0, 24, 5):
        matrizline = []
        for j in range(5):
            matrizline.append(mapline[i + j])
        mapmatriz.append(matrizline)

        # i= seria as colunas
        # j= seria as linhas

    inicio_partida(mapmatriz)


def inicio_partida(mapmatriz):

    ## posição inicial do jogador

   
    posicao = [4, 0]

    while True:

        jogador = verifica_cenario(posicao, mapmatriz)
        if jogador == "x":
            break
        print(jogador)

        # Formação do tabuleiro
        nova = (mapmatriz)
        nova[posicao[0]][posicao[1]] = "O"
        for linha in nova:
            print(linha)
            print()

        mov = str(input(" w = cima | a = esquerda | s = baixo | d = direita \n Insira o proxima jogada : "))

        if mov == "w" and posicao[0] != 0:
            posicao[0] -= 1
        if mov == "s" and posicao[0] != 5:
            posicao[0] += 1
        if mov == "a" and posicao[1] != 0:
            posicao[1] -= 1
        if mov == "d" and posicao[1] != 5:
            posicao[1] += 1


def verifica_cenario(posicao, mapmatriz):

    ## aqui e verificado se o jogador se posiciona sobre
    ## algum dos objetos que o fazem perder o game

    x = int(posicao[0])
    y = int(posicao[1])
    if mapmatriz[x][y] == "C" or mapmatriz[x][y] == "E":
        print("você perdeu!\n1 - voltar ao início\n2 - novo jogo\n---> ")
        op = str(input(""))
        if op == "1":
            inicio_partida(mapmatriz)
        if op == "2":
            novo_jogo()

    ## aqui eh verificado se o jogador venceu o jogo
    if mapmatriz[x][y] == "D":
        print("você venceu! \n Novo Jogo = 1 \n Sair= 2")
        ganhou = str(input(""))
        if ganhou == "1":
            inicio_partida(mapmatriz)
        if ganhou == "2":
            quit()


    ## aqui verificamos as posições adjacentes

    # acima
    if x - 1 > 0 and mapmatriz[x - 1][y] != " ":
        if mapmatriz[x - 1][y] == "E":
            print('--------------------')
            return " Está fedendo, Cuidado você está proximo do bixo grande"

        if mapmatriz[x - 1][y] == "C":
            print('--------------------')
            return "Cuidado você está proximo de um câniun"

            # direita
    if y + 1 < 5 and mapmatriz[x][y + 1] != " ":
        if mapmatriz[x][y + 1] == "E":
            print('--------------------')
            return "Está fedendo, Cuidado você está proximo do bixo grande"

        if mapmatriz[x][y + 1] == "C":
            print('--------------------')
            return "Cuidado você está proximo de um câniun"

    # abaixo
    if x + 1 < 5 and mapmatriz[x + 1][y] != " ":
        if mapmatriz[x + 1][y] == "E":
            print('--------------------')
            return "Está fedendo, Cuidado você está proximo do bixo grande"

        if mapmatriz[x + 1][y] == "C":
            print('--------------------')
            return "Cuidado você está proximo de um câniun"

            # esquerda
    if y - 1 > 0 and mapmatriz[x][y - 1] != " ":
        if mapmatriz[x][y - 1] == "E":
            print('--------------------')
            return "Está fedendo, Cuidado você está proximo do bixo grande"

        if mapmatriz[x][y - 1] == "C":
            print('--------------------')
            return "Cuidado você está proximo de um câniun"

    else:
        print('--------------------')
        print('O caminho está livre continue')
        print()

if _name_ == "_main_":
    main(_main_)
