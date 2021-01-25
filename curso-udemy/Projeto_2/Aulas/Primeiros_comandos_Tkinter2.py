# Documentação: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
from tkinter import *

# Instanciando a classe
janela = Tk()

# Comandos relacionados a janela de exibição
janela.title('Curso de Python')
janela.geometry('300x300')
janela.resizable(False, False)

# Entrada de dados
# Entry recebe por parâmetro o Pai dele
# função grid() é um gerenciador de layout
# O parâmentro show exibe um caracter específico ao invés do que está sendo digitado. Só aceita 2 caracter
Entry(janela, bg='gray', fg='white', show='*').grid(row=0, column=0)


# A função mainloop tem que ser invocada para que a aplicação entre no modo de tratamento de eventos
janela.mainloop()
