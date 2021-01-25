# Treeview é uma forma de se mostrar dados ao usuário, independente de onde e como a informação vem.
# Documentação: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Treeview.html
from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Curso de Python")
janela.resizable(False, False)

# O método Treeview recebeu por parâmetro a sua classe Pai, modo de seleção, as colunas que terá e como será exibida
# Os nomes passados no parâmetro coluna têm que ser o mesmo em tree.column
# Deve ser usar duplas aspas para não dar erro
# Select mode da as seguintes opções:
#                   selectmode='browse': O usuário pode selecionar um itens por vez com o mouse.
#                   selectmode='extended': O usuário pode selecionar vários itens por vez com o mouse.
#                   selectmode='none': O usuário  não pode selecionar itens com o mouse.

tree = ttk.Treeview(janela, selectmode="browse", column=("column1", "column2", "column3", "column4"), show="headings")

tree.column("column1", width=200, minwidth=50, stretch=NO)
tree.heading("#1", text="Nome")

tree.column("column2", width=100, minwidth=50, stretch=NO)
tree.heading("#2", text="Idade")

tree.column("column3", width=300, minwidth=50, stretch=NO)
tree.heading("#3", text="Endereço")

tree.column("column4", width=50, minwidth=50, stretch=NO)
tree.heading("#4", text="ID")

# Para inserir dados na treeview, usa-se o método insert()
# Insert recebe os parâmetros uma string vazia, END, values que deve ser uma tupla ou lista e tag com 1 de valor

dados = ["Tiago Lima", "23", "Rua Camburiu", 1], \
        ["Ana Santos", "19", "Rua México", 2], \
        ["Ryan Barbosa", "26", "Rua Castelo Branco", 3]

# Usando um laço para acessar e mostrar todos os dados na tupla dados
# END:O END inclui o valor no final da tree. Se vc coloca o parâmetro 1 ele sempre vai incluir na posição 1
# TAG: Seu programa pode associar uma ou mais cadeias de caracteres de tag a cada item. Você pode usar essas marcas
# para controlar a aparência de um item. Por exemplo, você pode marcar diretórios com a tag 'd' e arquivos com a tag
# 'f' e, a seguir, especificar que os itens com a tag 'd' usem uma fonte em negrito. Você também pode associar eventos
# a tags, de modo que certos eventos façam com que certos manipuladores sejam chamados para todos os itens que
# têm essa tag. Por exemplo, você pode configurar um navegador de arquivos para que, quando um usuário clica em um
# diretório, o navegador atualize seu conteúdo para refletir a estrutura do arquivo atual.
for dado in dados:
    tree.insert("", END, values=dado, tag=1)

tree.grid(row=0, column=0)
janela.mainloop()
