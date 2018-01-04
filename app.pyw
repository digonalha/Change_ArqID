"""Tela da aplicaçao de alteracao de arqid"""
from tkinter import Frame, Entry, Label, Button, Tk
import importlib
import change_arqid

class Application:
    """Montando a tela"""
    # pylint: disable=too-many-instance-attributes
    # Refatorarei essa classe no futuro. Dont be afraid may frendi
    def __init__(self, master=None):
        self.default_font = ("Segoe", "11")
        self.font_input = ("Arial", "10")
        self.create_title(master)
        self.create_frames(master)
        self.create_buttons(master)

    def create_title(self, master=None):
        """Criando o titulo da aplicacao"""

        self.lbl_titulo = Frame(master)
        self.lbl_titulo["pady"] = 10
        self.lbl_titulo.pack()

        self.titulo = Label(self.lbl_titulo, text="Alterar a instância no ArqID.txt")
        self.titulo["font"] = ("Arial", "11", "bold")
        self.titulo.pack()

    def create_frames(self, master=None):
        """Criando os frames(txtedits) da aplicacao"""

        self.txt_path_repository = Frame(master)
        self.txt_path_repository["padx"] = 20
        self.txt_path_repository.pack()

        self.repo_label = Label(self.txt_path_repository, text="Repositório",
                                font=self.default_font)
        self.repo_label.pack(side='left')

        self.path_repo = Entry(self.txt_path_repository)
        self.path_repo["width"] = 45
        self.path_repo["font"] = self.font_input
        self.path_repo['highlightbackground'] = "green"
        self.path_repo.pack(side='left')

        #--------------------------------------------

        self.txt_server = Frame(master)
        self.txt_server["padx"] = 20
        self.txt_server.pack()

        self.new_label = Label(self.txt_server, text="Servidor     ", font=self.default_font)
        self.new_label.pack(side='left')

        self.new_path = Entry(self.txt_server)
        self.new_path["width"] = 45
        self.new_path["font"] = self.font_input
        self.new_path.pack(side='left')

        #--------------------------------------------

        self.txt_station = Frame(master)
        self.txt_station["padx"] = 20
        self.txt_station.pack()

        self.new_label = Label(self.txt_station, text="Estaçao     ", font=self.default_font)
        self.new_label.pack(side='left')

        self.new_path = Entry(self.txt_station)
        self.new_path["width"] = 45
        self.new_path["font"] = self.font_input
        self.new_path.pack(side='left')

    def create_buttons(self, master=None):
        """Criando os botoes da aplicacao"""

        self.btn_container = Frame(master)
        self.btn_container["padx"] = 20
        self.btn_container["pady"] = 10
        self.btn_container.pack()

        self.mensagem = Label(self.btn_container, text="", font=self.default_font)
        self.mensagem.pack()

        self.btn_save_path = Button(self.btn_container, text="Salvar Path",
                                    font=self.default_font, width=12)
        self.btn_save_path.pack(side='left')

        self.btn_change_arqid = Button(self.btn_container, text="Alterar ArqID",
                                       font=self.default_font, width=12)
        self.btn_change_arqid['command'] = self.change_arqid_click
        self.btn_change_arqid.pack(side='left')

    def change_arqid_click(self):
        """Bot"""
        self.mensagem['text'] = ''
        resultado = change_arqid.alterar_arqid()
        self.mensagem['text'] = resultado
        importlib.reload(change_arqid) #gambiarra, descobrir outra forma de tratar isso

if __name__ == '__main__':
    APP = Tk()
    APP.title("Change ArqID - v0.1")
    X = (APP.winfo_screenwidth() - APP.winfo_reqwidth()) / 2
    Y = (APP.winfo_screenheight() - APP.winfo_reqheight()) / 2
    APP.geometry("+%d+%d" % (X, Y))
    APP.resizable(0, 0)
    Application(APP)
    APP.mainloop()
