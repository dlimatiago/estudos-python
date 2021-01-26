# https://www.tutorialspoint.com/python/python_gui_programming.htm
from typing import Union
from tkinter import *
from tkinter import messagebox
import pymysql.cursors
import pymysql as sql


class AdminWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Área do Administrador")
        self.root.geometry("600x600")
        self.root.mainloop()


class LoginWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Página de Inicial")
        self.root.geometry("520x150")

        # LabelFrame
        self.LbFrame = LabelFrame(self.root, text="Sistema", labelanchor="n", borderwidth=1, relief="solid")
        self.LbFrame.place(x=10, y=10, width=500, height=120)

        # Labels
        Label(self.LbFrame, text="Usuário", padx=5, pady=5).grid(row=0, column=0, sticky="w")
        Label(self.LbFrame, text="Senha", padx=5, pady=5).grid(row=1, column=0, sticky="w")

        # Entry
        self.user = Entry(self.LbFrame, width=30, relief="solid")
        self.user.grid(row=0, column=1)
        self.password = Entry(self.LbFrame, show="*", width=30, relief="solid")
        self.password.grid(row=1, column=1)

        # Buttons
        self.login = Button(self.LbFrame, text="Logar", bg="green", fg="black", width=15, command=self._loginValidation)
        self.login.grid(row=0, column=4, padx=100, pady=10)

        self.singupButton = Button(self.LbFrame, text="Cadastrar", bg="orange", fg='black', width=15)
        self.singupButton.grid(row=1, column=4, padx=100, pady=10)

        self.root.mainloop()

    def _loginValidation(self):
        authenticated = superUser = False
        user = self.user.get()
        password = self.password.get()

        usersfound = self._query("select * from cadastros", "fetchall")
        if usersfound is not None:
            for users in usersfound:
                values = users.values()
                if user in values and password in values:
                    if 2 in values:
                        superUser = True
                    authenticated = True
                    break
                else:
                    authenticated = False
            if not authenticated:
                messagebox.showinfo("Login inválido", "❌ Senha/usuário não costam no Banco de Dados ❌")
            if authenticated:
                # Fazer uma progressbar ou loading screen
                self.root.destroy()
                messagebox.showinfo("Login", f"Olá, {user}")
                if superUser:
                    AdminWindow()

    def _query(self, line: str, action: str = "commit") -> Union[bool, str, dict, None]:
        try:
            connect = sql.connect(
                host="localhost",
                port=3308,
                user="root",
                password="4321.",
                db="erp",
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor
            )

            with connect.cursor() as cursor:
                cursor.execute(line)
            if action == "commit":
                try:
                    connect.commit()
                    return True
                except:
                    messagebox.showinfo("Erro", "❌ Erro ao inserir/deletar os dados ❌")
                    return None
            elif action == "fetchall":
                return cursor.fetchall()
        except pymysql.err.ProgrammingError:
            messagebox.showinfo("Erro", "❌ Erro na query ❌")
        except pymysql.err.OperationalError or ConnectionError or ConnectionRefusedError or ConnectionAbortedError:
            messagebox.showinfo("Erro", "❌ Não foi possível se comunicar com o Banco de Dados ❌")
            self.root.destroy()



def validation(phrase, typo="int", options=None):
    while True:
        try:

            if typo == "int":
                answer = int(input(phrase))
            elif typo == "float":
                answer = float(input(phrase))
            elif typo == "str":
                answer = input(phrase).strip().lower()[:1]
        except ValueError:
            messagebox.showinfo("Erro", "❌ Tipo de dado incorreto ❌")
            continue
        else:
            if options is not None:
                while True:
                    if answer in options:
                        return answer
                    else:
                        messagebox.showinfo("Erro", "❌ Opção inválida ❌")
                        break
            else:
                return answer
            continue


LoginWindow()
