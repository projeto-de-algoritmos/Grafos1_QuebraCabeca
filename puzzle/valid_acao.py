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