# Quebra-Cabeça - Puzzle 8

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2045268  | Raquel Temóteo Eucaria Pereira da Costa|
| 20/0026046  |  Pedro de Oliveira Campos Barbosa |

## Sobre 
<!-- Descreva os objetivos do seu projeto e como ele funciona.  -->

O projeto tem como objetivo construir um jogo puzzle de 8 peças fazendo uso da **Busca em Largura (BFS)**, estudado na disciplina de Projeto de Algoritmo.

A busca em largura é usada para resolver o puzzle quando o usuário não quser resolver sozinho.

A busca em largura oferece o menor caminho para o estado objetivo. Com base nos movimentos possíveis da peça 0, é gerado os grafos filhos, até chegar no desejado.

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*mQ6ODKhGqh3ZVCDo7A1XDw.jpeg)

![](https://web.cs.wpi.edu/~heineman/html/teaching_/cs2223/b15/days/dfs_8puzzle.png)


## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python<br>

**Dependências**
- Python 3.9.0 ou superior
  
**Execução**
- Clone o projeto (ou baixe):
  
  ```shell
  git clone https://github.com/projeto-de-algoritmos/Grafos1_QuebraCabeca.git 
  && cd Grafos1_QuebraCabeca/
  ```

 - Execute o arquivo principal ```puzzleGUI.py```:
  
    ```shell
    python puzzleGUI.py 
    ```


## Uso 
1. Clique no botão "Jogar" 
2. Clique na posição que deseja movimentar a peça 0 (branca).
   - **Opções**: Dependendo você pode moviemntar oara **cima**, para **baixo**, para **esquerda** ou **direita**
3. Caso queira que o computador resolva, clique no botão resolver, o a busca em largura (BFS) será acionada.

  



