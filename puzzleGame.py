import os
import random

class PuzzleDoJogo:
    def __init__(self):
        # Declarando o estadoInicial e estadoObjetivo do puzzle

        estados_iniciais = [
            [[4, 7, 5], [2, 0, 8], [3, 1, 6]],  # teste 1
            [[3, 2, 0], [6, 7, 5], [4, 1, 8]],  # teste 2
            [[0, 3, 6], [1, 2, 4], [7, 8, 5]],  # teste 3
            [[6, 2, 5], [8, 7, 4], [0, 1, 3]]   # teste 4
        ]

        self.estadoInicial = random.choice(estados_iniciais)

        self.estadoObjetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def imprimir_estado(self, estado_atual):
        if estado_atual is None:
            return

        for i in range(len(estado_atual)):
            for j in range(len(estado_atual[0])):
                if estado_atual[i][j] == '0':
                    print(" ", end=" ")
                else:
                    print(estado_atual[i][j], end=" ")
            print()
        print()
    
    def to_list(self):
        estado = []
        for i in range(len(self.estadoInicial)):
            for j in range(len(self.estadoInicial[0])):
                estado.append(self.estadoInicial[i][j])
        return estado

    def clear(self):
        os.system('clear')

    def validar(self):
        if self.estadoInicial == self.estadoObjetivo:
            return True

    def troca_posicao(self, direcao):
        estado_atual = self.estadoInicial
        
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

        for i in range(len(estado_atual)):
            for j in range(len(estado_atual[0])):
                if estado_atual[i][j] == 0:
                    posicaoI0 = i
                    posicaoJ0 = j
                    break
        try:
            if (posicaoI0 + incV) < 0 or (posicaoJ0 + incH) < 0:
                raise
            else:
                estado_atual[posicaoI0][posicaoJ0] = estado_atual[posicaoI0 + incV][posicaoJ0 + incH]
                estado_atual[posicaoI0 + incV][posicaoJ0 + incH] = 0
        except:
            print("Movimento inválido")
            # mostrando exception

        # self.imprimir_estado(estado_atual)
        self.estadoInicial = estado_atual

    def main_loop(self):
        while True:
            self.validacao(self.estadoInicial, self.estadoObjetivo)
            escolha = input('Use wasd para movimentar o espaço vazio, e pressione Enter para confirmar:\n')
            self.clear()

            if escolha == "":
                break
            else:
                self.troca_posicao(escolha)

if __name__ == "__main__":
    jogo = PuzzleDoJogo()
    print(jogo.estadoInicial)
    jogo.troca_posicao("d")
    print(jogo.estadoInicial)
