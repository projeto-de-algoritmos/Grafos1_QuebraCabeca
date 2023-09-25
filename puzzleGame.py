import os

# declarando o estadoInicial e estadoObjetivo (estadoObjetivo) do puzzle
estadoInicial = [['4','7','5'],['2','0','8'],['3','1','6']]
estadoObjetivo = [['1','2','3'],['4','5','6'],['7','8','0']]

def imprimirEstado(estadoAtual):
    for i in range(len(estadoAtual)):
        for j in range(len(estadoAtual[0])):
            if estadoAtual[i][j] == '0':
                print(" ", end=" ")
            else:
                print(estadoAtual[i][j], end=" ")
        print()
    print()

imprimirEstado(estadoInicial)

# limpa a tela do terminal
def clear():
    os.system('clear')

# compara o estado atual do puzzle com o estado estadoObjetivo
def validacao(estadoAtual, estadoObjetivo):
    if estadoAtual == estadoObjetivo:
        print("Congratulations!")
        exit()

# recebe o estado atual e a direcao que o 0 vai se locomover
def trocaPosicao(estadoAtual, direcao):

    # define a direcao que o 0 vai de acordo com as variaveis incrementoVertical (incV) e incrementoHorizontal (incH)
    if direcao == "direita" or direcao == "d":
        incV = 0
        incH = 1
    elif direcao == "cima" or direcao == "w":
        incV = -1
        incH = 0
    elif direcao == "esquerda" or direcao == "a":
        incV = 0
        incH = -1
    elif direcao == "baixo" or direcao == "s":
        incV = 1
        incH = 0

    # acha as coordenadas do 0 no estadoAtual
    for i in range(len(estadoAtual)):
        for j in range(len(estadoAtual[0])):
            if estadoAtual[i][j] == '0':
                posicaoI0 = i
                posicaoJ0 = j
                break

    try:
        # impede que haja qualquer movimento fora do comum do puzzle. 
        # incV e incH sao os incrementos vertical e horizontal, respectivamente.
        if (posicaoI0 + incV) < 0 or (posicaoJ0 + incH) < 0:
            raise 
        else:
            # troca de posicao do zero com o valor presente na posicao que ele ira ocupar
            estadoAtual[posicaoI0][posicaoJ0] = estadoAtual[posicaoI0 + incV][posicaoJ0 + incH]
            estadoAtual[posicaoI0 + incV][posicaoJ0 + incH] = '0'
    except:
        print("movimento invalido")

    imprimirEstado(estadoAtual)
    
    return estadoAtual

def mainLoop(estadoInicial, estadoObjetivo):
    while True:
        validacao(estadoInicial, estadoObjetivo)
        escolha = input('Use wasd para movimentar o espaco vazio, e de Enter para confirmar:\n')
        clear()

        if escolha == "":
            break
        else:
            estadoInicial = trocaPosicao(estadoInicial, escolha)

mainLoop(estadoInicial, estadoObjetivo)
