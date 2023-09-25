import tkinter as tk
from PIL import Image, ImageTk
import puzzleGame as pg
import bfs
from time import sleep

class JogoPuzzleInterface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo de Puzzle")
        self.janela.geometry("600x600")
        self.frame_inicial = tk.Frame(self.janela)
        self.frame_inicial.pack()
        self.criar_frame_inicial()

        self.jogo = None
        self.ordem_imagens = None
        self.imagem_widgets = {}

    def criar_frame_inicial(self):
        label = tk.Label(self.frame_inicial, text="Bem-vindo ao Jogo de Puzzle")
        label.pack(pady=20)

        botao_jogar = tk.Button(self.frame_inicial, text="Jogar", command=self.iniciar_jogo)
        botao_jogar.pack()

        botao_sair = tk.Button(self.frame_inicial, text="Sair", command=self.janela.quit)
        botao_sair.pack()

    def iniciar_jogo(self):
        self.frame_inicial.destroy()
        self.frame = tk.Frame(self.janela)
        self.frame.pack()

        # Adicionar o botão "Resolver"
        botao_resolver = tk.Button(self.frame, text="Resolver", command=self.resolver_jogo)
        botao_resolver.grid(row=3, column=1, pady=10)

        # Resto do código da interface do jogo...
        self.carregar_jogo()

    def carregar_jogo(self):
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

        self.jogo = pg.PuzzleDoJogo()
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

    def resolver_jogo(self):
        movimentos = bfs.main(bfs, self.jogo.to_list())
        movimentos = bfs.acoes
        # print(movimentos)
        for i in movimentos:
            self.jogo.troca_posicao(i)
            self.ordem_imagens = self.jogo.estadoInicial
            self.atualizar_ordem()

    def atualizar_ordem(self):
        global ordem_imagens
        ordem_imagens = self.jogo.estadoInicial
        for posicao, widget in self.imagem_widgets.items():
            widget.grid_forget()
            i, j = self.encontrar_posicao_widget(posicao)
            widget.grid(row=i, column=j, padx=5, pady=5)
        
        if self.verificar_vitoria():
            self.exibir_parabenizacao()

    def encontrar_posicao_widget(self, posicao):
        for i in range(3):
            for j in range(3):
                if self.ordem_imagens[i][j] == posicao:
                    return i, j

    def verificar_vitoria(self):
        return self.jogo.validar()

    def exibir_parabenizacao(self):
        parabenizacao = tk.Toplevel(self.janela)
        parabenizacao.title("Parabéns!")

        mensagem = tk.Label(parabenizacao, text="Você venceu o jogo!")
        mensagem.pack(pady=20)

        botao_ok = tk.Button(parabenizacao, text="OK", command=self.finalizar_jogo)
        botao_ok.pack()

    def finalizar_jogo(self):
        self.janela.destroy()

    def executar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = JogoPuzzleInterface()
    app.executar()
