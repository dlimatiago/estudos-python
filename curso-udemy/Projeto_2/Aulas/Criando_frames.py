# Um frame é basicamente apenas um contêiner para outros widgets. A janela raiz do seu aplicativo é basicamente um
# frame. Cada frame tem seu próprio layout de grade, de modo que a grade de widgets em cada frame funciona de
# forma independente.
# Os widgets de frames são uma ferramenta valiosa para tornar seu aplicativo modular.
# Você pode agrupar um conjunto de widgets relacionados em um widget composto, colocando-os em um frame. Melhor ainda,
# você pode declarar uma nova classe que herda de Frame, adicionando sua própria interface a ela. Essa é uma boa maneira
# de ocultar os detalhes das interações dentro de um grupo de widgets relacionados do mundo externo.

# Documentação: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/frame.html
from tkinter import *

janela = Tk()
janela.title("Criando um Frame")
janela.geometry("500x500")
janela.resizable(False, False)

frame = Frame(janela, width=300, height=300, bg='purple').grid(row=0, column=0)
Label(frame, text="Teste do Frame", fg='white', bg='purple').grid(row=0, column=0)

janela.mainloop()
