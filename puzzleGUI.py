import tkinter as tk
from PIL import Image, ImageTk
import testeGrafo as tg

# Lista de 9 imagens (substitua esses caminhos pelos caminhos reais das suas imagens)
imagens = [
    "./s/imagem_1.png",
    "./_temp/imagem_2.png",
    "./_temp/imagem_3.png",
    "./_temp/imagem_4.png",
    "./_temp/imagem_5.png",
    "./_temp/imagem_6.png",
    "./_temp/imagem_7.png",
    "./_temp/imagem_8.png",
    "./_temp/imagem_9.png"
]

# Lista que representa a ordem inicial das imagens
jogo = tg.PuzzleDoJogo()
ordem_imagens = jogo.estadoInicial

# Posição da imagem 0
posicao_imagem_0 = (0, 0)

def criar_interface():
    janela = tk.Tk()
    janela.title("Interface com 9 Imagens")

    imagem_widgets = {}
    
    for i in range(3):
        for j in range(3):
            posicao = ordem_imagens[i][j]
            if posicao == 0:
                continue
            caminho_imagem = imagens[posicao - 1]

            imagem = Image.open(caminho_imagem)
            imagem = imagem.resize((100, 100), Image.LANCZOS)
            imagem = ImageTk.PhotoImage(imagem)
            
            imagem_widget = tk.Label(janela, image=imagem)
            imagem_widget.image = imagem
            imagem_widget.grid(row=i, column=j, padx=5, pady=5)

            imagem_widgets[posicao] = imagem_widget

    def clicar_imagem(event, estadoAtual=ordem_imagens, janela=janela):
        posicao_imagem_0 = [0, 0]

        for i in range(len(estadoAtual)):
            for j in range(len(estadoAtual[0])):
                if estadoAtual[i][j] == 0:
                    posicao_imagem_0[0] = i
                    posicao_imagem_0[1] = j
                    break
        
        # print(posicao_imagem_0[0], posicao_imagem_0[1])

        for posicao, widget in imagem_widgets.items():
            if widget == event.widget:
                global ordem_imagens
                currentRow, currentCollumn = widget.grid_info()['row'], widget.grid_info()['column']

                if currentRow == posicao_imagem_0[0] - 1 and currentCollumn == posicao_imagem_0[1]:
                    print("Cima")
                    jogo.troca_posicao("cima")
                elif currentRow == posicao_imagem_0[0] + 1 and currentCollumn == posicao_imagem_0[1]:
                    print("Baixo")
                    jogo.troca_posicao("baixo")

                elif currentRow == posicao_imagem_0[0] and currentCollumn == posicao_imagem_0[1] - 1:
                    print("Esquerda")
                    jogo.troca_posicao("esquerda")
                elif currentRow == posicao_imagem_0[0] and currentCollumn == posicao_imagem_0[1] + 1:
                    print("Direita")
                    jogo.troca_posicao("direita")
                else:
                    break
                ordem_imagens = jogo.estadoInicial
                atualizar_ordem(janela)
                break

    for widget in imagem_widgets.values():
        widget.bind("<Button-1>", clicar_imagem)

    janela.mainloop()

def atualizar_ordem(janela):
    global ordem_imagens, posicao_imagem_0
    posicao_imagem_0 = (0, 0)
    # janela.update()
    # janela.update_idletasks()
    janela.destroy()
    criar_interface()

if __name__ == "__main__":
    criar_interface()
