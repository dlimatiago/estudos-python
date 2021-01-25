from tkinter import *


def imc():
    peso = float(ent_peso.get())
    altura = float(ent_altura.get())
    _imc = peso / altura ** 2
    lb_resposta['text'] = f'{_imc:.1f}'


janela = Tk()

janela.title('Cálculo de IMC')
janela.geometry('280x140')  # Comp x Altura
janela.resizable(False, False)

# Atributos
lb_titulo = Label(janela, text='Calcule seu IMC')
lb_peso = Label(janela, text='Informe seu peso (kg)')
lb_altura = Label(janela, text='Informe sua altura (m)')
ent_peso = Entry(janela)
ent_altura = Entry(janela)
btn_calcular = Button(janela, text='Calcular', bg='black', fg='white', command=imc)
lb_resposta = Label(janela, text='-')

# Exibição
lb_titulo.grid(row=0, column=0, columnspan=2)
lb_peso.grid(row=1, column=0, sticky='w')
ent_peso.grid(row=1, column=1)
lb_altura.grid(row=2, column=0, sticky='w')
ent_altura.grid(row=2, column=1)
btn_calcular.grid(row=3, column=0, pady=15)
lb_resposta.grid(row=3, column=1, pady=15)

janela.mainloop()
