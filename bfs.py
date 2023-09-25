import time
import timeit
from collections import deque
from puzzle.valid_acao import acao
import puzzleGame as pg

# Estado do puzzle
class PuzzleEstado:
    def __init__(self, estado, pai, acao, largura, custo, chave):
        self.estado = estado # estado atual 
        self.pai = pai # estado anterior
        self.acao = acao # cima, para baixo, esquerda, direita
        self.largura = largura # Na árvore de busca
        self.custo = custo # Custo acumulado até este nó
        self.chave = chave # Chave usada para ordenar os nós
        self.acoes = [] # Ações possíveis

        # Se o estado atual não for nulo, converte a matriz em uma string
        if self.estado:
            self.map = ''.join(str(e) for e in self.estado)
    
    # comparacao de puzzle
    def __eq__(self, other): 
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map

    # converte em string o puzzle
    def __str__(self): 
        return str(self.map)    

Goalestado = [1, 2, 3, 4, 5, 6, 7, 8, 0] # Puzzle objetivo
GoalNode = None # Nó encontrado
NodesExpanded = 0 # total de nós visitados
MaxSearchDeep = 0 # largura (camadas)
MaxFrontier = 0 # fila de nós a serem explorados

########## BFS ############

def bfs(startEstado):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited= set() # estados visitados = evita loop
    Queue = deque([PuzzleEstado(startEstado, None, None, 0, 0, 0)]) # fila com os estados a serem explorados

    while Queue: # enquanto nao estiver vazia
        node = Queue.popleft() # reacao o no da fila
        boardVisited.add(node.map) # add em visitados
        if node.estado == Goalestado:
            GoalNode = node
            return Queue
        posiblePaths = subNodes(node) # gera os estados filhos
        for path in posiblePaths: #itera sobre os estados filhos
            if path.map not in boardVisited: # verifica se nao foi visitado 
                Queue.append(path) # add queue
                boardVisited.add(path.map)
                if path.largura > MaxSearchDeep: 
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize

###################
    
# cria novos objetos puzzle para cada possivel movimento
def subNodes(node): 

    global NodesExpanded
    NodesExpanded = NodesExpanded+1

    nextPaths = [] #filhos possiveis
    nextPaths.append(PuzzleEstado(acao(node.estado, 1), node, 1, node.largura + 1, node.custo + 1, 0)) #cima
    nextPaths.append(PuzzleEstado(acao(node.estado, 2), node, 2, node.largura + 1, node.custo + 1, 0)) #baixo
    nextPaths.append(PuzzleEstado(acao(node.estado, 3), node, 3, node.largura + 1, node.custo + 1, 0)) #esquerda
    nextPaths.append(PuzzleEstado(acao(node.estado, 4), node, 4, node.largura + 1, node.custo + 1, 0)) #direita
    
    nodes=[] # salva os estados validos 
    
    # verifica se eh valido
    for procPaths in nextPaths:
        if(procPaths.estado!=None):
            nodes.append(procPaths)
    return nodes


def print_estado(estado):
    for i in range(3):
        for j in range(3):
            print(estado[i * 3 + j], end=' ')
        print()


def main(self, estadoAtual):

    global GoalNode

    # Estado inicial em lista
    #data = [4, 7, 5, 2, 0, 8, 3, 1, 6]
    
    # Estado Puzzle convertido
    Initialestado = []
    #Initialestado = [int(data[i]) for i in range(9)]
    Initialestado = estadoAtual  

    # Inicio contagem do tempo
    start = timeit.default_timer()

    bfs(Initialestado)

    # Fim contagem do tempo
    stop = timeit.default_timer()
    time = stop - start

    # Salvando resultado
    deep = GoalNode.largura
    acaos = []
    estados = []

    # Adicione o estado inicial à lista de estados
    estados.append(Initialestado)

    while Initialestado != GoalNode.estado:
        if GoalNode.acao == 1:
            path = 'cima'
        if GoalNode.acao == 2:
            path = 'baixo'
        if GoalNode.acao == 3:
            path = 'esquerda'
        if GoalNode.acao == 4:
            path = 'direita'
        acaos.insert(0, path)
        estados.insert(0, GoalNode.estado)  # Adicione o estado atual à lista de estados
        GoalNode = GoalNode.pai

    # Resultado
    print(Initialestado)
    print("Estado Inicial: ")
    print_estado(Initialestado)
    print("\n\n")

    cont = 1
    for i in range(len(acaos)):
        print(cont)
        print(f"Ação: {acaos[i]}")
        print("Estado:")
        print_estado(estados[i])
        print("\n")
        cont+=1

    print("-----Informações------\n\n")

    self.acoes = acaos

    print("Caminho: ",acaos)
    print("Custo: ", len(acaos))
    print("Nós visitados: ", str(NodesExpanded))
    print("Procuras: ", str(deep))
    print("Camadas: ", str(MaxSearchDeep))
    print("Tempo de execução: {:.3f} segundos".format(time))

    print("\n-----FIM-----\n")

if __name__ == '__main__':
    main()

