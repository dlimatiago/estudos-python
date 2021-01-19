from tkinter import *

# Instanciando a classe
janela = Tk()

# Comandos relacionados a janela de exibição
janela.title('Minha primeira janela')
janela.geometry('800x400')
janela.resizable(False, False)

# Criando uma caixa de texto, precisa dizer a classe Pai dela pra saber onde ela será pertencente
# Text exibe um texto
# bg altera a cor do fundo
# fb altera a cor da fonte
# Padx da um espaçamento no eixo x e Pady no eixo y
# função grid() é um gerenciador de layout
Label(janela, text='Olá mundo!', bg='black', fg='white', padx=30, pady=30).grid(row=0, column=0)

# A função mainloop tem que ser invocada para que a aplicação entre no modo de tratamento de eventos
janela.mainloop()
