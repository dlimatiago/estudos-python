# Documentação: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
from tkinter import *


def show():
    armazenarLabel['text'] = 'Botão foi clicado'


# Instanciando a classe
janela = Tk()

# Comandos relacionados a janela de exibição
janela.title('Curso de Python')
janela.geometry('300x300')
janela.resizable(False, False)

# Criando botões
# Como sempre, passando o Pai dele, onde esse botão estará
# Parâmetro text informa o texto que aparece no botão
# heigt e width são parâmetros que mexem nas dimensões do botão
# O parâmetro command executa algo quando se clica no botão
# O parâmetro sticky move para cima(n), baixo(s), esquerda(w) ou direita(e) (função grid)


Button(janela, text='Clique aqui', bg='yellow', fg='black', height=10, width=20, command=show).grid(row=0, column=0)
armazenarLabel = Label(janela, text='Botão não foi clicado')
# Quando o botão é pressionado, a propriedade text é alterada na função show atraves do parametro command
armazenarLabel.grid(row=1, column=0, sticky='w')

# A função mainloop tem que ser invocada para que a aplicação entre no modo de tratamento de eventos
janela.mainloop()
