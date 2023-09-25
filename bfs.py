import time
import timeit
from collections import deque

# Estado do puzzle
class PuzzleEstado:
    def __init__(self, estado, pai, acao, largura, custo, chave):
        self.estado = estado # estado atual 
        self.pai = pai # estado anterior
        self.acao = acao # cima, para baixo, esquerda, direita
        self.largura = largura # Na árvore de busca
        self.custo = custo # Custo acumulado até este nó
        self.chave = chave # Chave usada para ordenar os nós

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


Goalestado = [0, 1, 2, 3, 4, 5, 6, 7, 8] # Puzzle objetivo
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

#Movimentacao do Puzzle
def acao(estado, direction):
    
    # Copia do estado atual
    newestado = estado[:]  
    
    #Posicao do 0
    index = newestado.index(0)

    # 1 - cima
    # 2 - baixo
    # 3 - esquerda
    # 4 - direita

    # movimentos validos
    if(index==0):
        if(direction==1):
            return None
        if(direction==2):
            temp=newestado[0]
            newestado[0]=newestado[3]
            newestado[3]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newestado[0]
            newestado[0]=newestado[1]
            newestado[1]=temp
        return newestado      
    if(index==1):
        if(direction==1):
            return None
        if(direction==2):
            temp=newestado[1]
            newestado[1]=newestado[4]
            newestado[4]=temp
        if(direction==3):
            temp=newestado[1]
            newestado[1]=newestado[0]
            newestado[0]=temp
        if(direction==4):
            temp=newestado[1]
            newestado[1]=newestado[2]
            newestado[2]=temp
        return newestado    
    if(index==2):
        if(direction==1):
            return None
        if(direction==2):
            temp=newestado[2]
            newestado[2]=newestado[5]
            newestado[5]=temp
        if(direction==3):
            temp=newestado[2]
            newestado[2]=newestado[1]
            newestado[1]=temp
        if(direction==4):
            return None
        return newestado
    if(index==3):
        if(direction==1):
            temp=newestado[3]
            newestado[3]=newestado[0]
            newestado[0]=temp
        if(direction==2):
            temp=newestado[3]
            newestado[3]=newestado[6]
            newestado[6]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newestado[3]
            newestado[3]=newestado[4]
            newestado[4]=temp
        return newestado
    if(index==4):
        if(direction==1):
            temp=newestado[4]
            newestado[4]=newestado[1]
            newestado[1]=temp
        if(direction==2):
            temp=newestado[4]
            newestado[4]=newestado[7]
            newestado[7]=temp
        if(direction==3):
            temp=newestado[4]
            newestado[4]=newestado[3]
            newestado[3]=temp
        if(direction==4):
            temp=newestado[4]
            newestado[4]=newestado[5]
            newestado[5]=temp
        return newestado
    if(index==5):
        if(direction==1):
            temp=newestado[5]
            newestado[5]=newestado[2]
            newestado[2]=temp
        if(direction==2):
            temp=newestado[5]
            newestado[5]=newestado[8]
            newestado[8]=temp
        if(direction==3):
            temp=newestado[5]
            newestado[5]=newestado[4]
            newestado[4]=temp
        if(direction==4):
            return None
        return newestado
    if(index==6):
        if(direction==1):
            temp=newestado[6]
            newestado[6]=newestado[3]
            newestado[3]=temp
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            temp=newestado[6]
            newestado[6]=newestado[7]
            newestado[7]=temp
        return newestado
    if(index==7):
        if(direction==1):
            temp=newestado[7]
            newestado[7]=newestado[4]
            newestado[4]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newestado[7]
            newestado[7]=newestado[6]
            newestado[6]=temp
        if(direction==4):
            temp=newestado[7]
            newestado[7]=newestado[8]
            newestado[8]=temp
        return newestado
    if(index==8):
        if(direction==1):
            temp=newestado[8]
            newestado[8]=newestado[5]
            newestado[5]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newestado[8]
            newestado[8]=newestado[7]
            newestado[7]=temp
        if(direction==4):
            return None
        return newestado

def print_estado(estado):
    for i in range(3):
        for j in range(3):
            print(estado[i * 3 + j], end=' ')
        print()

def main():

    global GoalNode

    # Estado inicial em lista
    data = [4, 7, 5, 2, 0, 8, 3, 1, 6]

    # Estado Puzzle convertido
    Initialestado = []
    Initialestado = [int(data[i]) for i in range(9)]

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
            path = 'Cima'
        if GoalNode.acao == 2:
            path = 'Baixo'
        if GoalNode.acao == 3:
            path = 'Esquerda'
        if GoalNode.acao == 4:
            path = 'Direita'
        acaos.insert(0, path)
        estados.insert(0, GoalNode.estado)  # Adicione o estado atual à lista de estados
        GoalNode = GoalNode.pai



    # Resultado
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

    # print("Caminho: ",acaos)
    print("Custo: ", len(acaos))
    print("Nós visitados: ", str(NodesExpanded))
    print("search_largura: ", str(deep))
    print("MaxSearchDeep: ", str(MaxSearchDeep))
    print("Tempo de execução: {:.3f} segundos".format(time))

    print("\n-----FIM----\n")

if __name__ == '__main__':
    main()

