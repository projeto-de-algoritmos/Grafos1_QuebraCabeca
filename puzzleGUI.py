import tkinter as tk
from PIL import Image, ImageTk
import testeGrafo as tg

class JogoPuzzleInterface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Interface com 9 Imagens")
        self.frame = tk.Frame(self.janela)
        self.frame.pack()

        # Lista de 9 imagens (substitua esses caminhos pelos caminhos reais das suas imagens)
        self.imagens = [
            "./src/imagem_1.png",
            "./src/imagem_2.png",
            "./src/imagem_3.png",
            "./src/imagem_4.png",
            "./src/imagem_5.png",
            "./src/imagem_6.png",
            "./src/imagem_7.png",
            "./src/imagem_8.png",
            "./src/imagem_9.png"
        ]

        # Lista que representa a ordem inicial das imagens
        self.jogo = tg.PuzzleDoJogo()
        self.ordem_imagens = self.jogo.estadoInicial

        self.imagem_widgets = {}
        self.criar_interface(self.ordem_imagens)

    def criar_interface(self, ordem_atual):
        for i in range(3):
            for j in range(3):
                posicao = ordem_atual[i][j]
                if posicao == 0:
                    continue
                caminho_imagem = self.imagens[posicao - 1]

                imagem = Image.open(caminho_imagem)
                imagem = imagem.resize((100, 100), Image.LANCZOS)
                imagem = ImageTk.PhotoImage(imagem)
                
                imagem_widget = tk.Label(self.frame, image=imagem)
                imagem_widget.image = imagem
                imagem_widget.grid(row=i, column=j, padx=5, pady=5)

                self.imagem_widgets[posicao] = imagem_widget

        for widget in self.imagem_widgets.values():
            widget.bind("<Button-1>", self.clicar_imagem)

    def clicar_imagem(self, event):
        posicao_imagem_0 = [0, 0]

        for i in range(len(self.ordem_imagens)):
            for j in range(len(self.ordem_imagens[0])):
                if self.ordem_imagens[i][j] == 0:
                    posicao_imagem_0[0] = i
                    posicao_imagem_0[1] = j
                    break
        
        for posicao, widget in self.imagem_widgets.items():
            if widget == event.widget:
                currentRow, currentCollumn = widget.grid_info()['row'], widget.grid_info()['column']

                if currentRow == posicao_imagem_0[0] - 1 and currentCollumn == posicao_imagem_0[1]:
                    print("Cima")
                    self.jogo.troca_posicao("cima")
                elif currentRow == posicao_imagem_0[0] + 1 and currentCollumn == posicao_imagem_0[1]:
                    print("Baixo")
                    self.jogo.troca_posicao("baixo")

                elif currentRow == posicao_imagem_0[0] and currentCollumn == posicao_imagem_0[1] - 1:
                    print("Esquerda")
                    self.jogo.troca_posicao("esquerda")
                elif currentRow == posicao_imagem_0[0] and currentCollumn == posicao_imagem_0[1] + 1:
                    print("Direita")
                    self.jogo.troca_posicao("direita")
                else:
                    break
                self.ordem_imagens = self.jogo.estadoInicial
                self.atualizar_ordem()

    def atualizar_ordem(self):
        global ordem_imagens
        ordem_imagens = self.jogo.estadoInicial
        for posicao, widget in self.imagem_widgets.items():
            widget.grid_forget()  # Remove o widget da grid
            # Recria o widget com a nova posição
            i, j = self.encontrar_posicao_widget(posicao)
            widget.grid(row=i, column=j, padx=5, pady=5)

    def encontrar_posicao_widget(self, posicao):
        for i in range(3):
            for j in range(3):
                if self.ordem_imagens[i][j] == posicao:
                    return i, j

    def executar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = JogoPuzzleInterface()
    app.executar()
