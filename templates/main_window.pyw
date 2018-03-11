"""Tela da aplicaçao de alteracao de arqid"""
from tkinter import Frame, Entry, Label, Button, Checkbutton, IntVar
import importlib
import sys
from modules import change_arqid

sys.path.append("..")

class CreateInterface:
    """Montando a tela"""
    # pylint: disable=too-many-instance-attributes
    # Refatorarei essa classe no futuro. Dont be afraid may frendi

    def __init__(self, master=None):
        self.etrade_checked = IntVar()
        self.default_font = ("Segoe", "11")
        self.font_input = ("Arial", "10")
        self.create_title(master)
        self.create_frames(master)
        self.create_check_boxes(master)        
        self.create_buttons(master)
        self.load_paths()

    def create_title(self, master=None):
        """Criando o titulo da aplicacao"""

        self.lbl_titulo = Frame(master)
        self.lbl_titulo["pady"] = 10
        self.lbl_titulo.pack()

        self.titulo = Label(self.lbl_titulo, text="Alterar Instância")
        self.titulo["font"] = ("Arial", "11", "bold")
        self.titulo.pack()

    def create_frames(self, master=None):
        """Criando os frames(txtedits) da aplicacao"""

        #--------------------REPOSITORIO-----------------

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

        #---------------------SERVIDOR-----------------

        self.txt_server = Frame(master)
        self.txt_server["padx"] = 20
        self.txt_server.pack()

        self.new_label = Label(self.txt_server, text="Servidor     ", font=self.default_font)
        self.new_label.pack(side='left')

        self.instance_server = Entry(self.txt_server)
        self.instance_server["width"] = 45
        self.instance_server["font"] = self.font_input
        self.instance_server.pack(side='left')

        #----------------------ESTAÇÃO------------------

        self.txt_station = Frame(master)
        self.txt_station["padx"] = 20
        self.txt_station.pack()

        self.new_label = Label(self.txt_station, text="Estação     ", font=self.default_font)
        self.new_label.pack(side='left')

        self.instance_station = Entry(self.txt_station)
        self.instance_station["width"] = 45
        self.instance_station["font"] = self.font_input
        self.instance_station.pack(side='left')

    def create_buttons(self, master=None):
        """Criando os botoes da aplicacao"""

        self.txt_container = Frame(master)
        self.txt_container.pack()

        self.btn_container = Frame(master)
        self.btn_container["padx"] = 20
        self.btn_container["pady"] = 10
        self.btn_container.pack()

        self.txt_status = Label(self.txt_container, text="Instância atual")
        self.txt_status["font"] = ("Arial", "9", "bold")
        self.txt_status.pack(side='top')
        self.mensagem = Label(self.txt_container, text="")
        self.mensagem.pack(side='right')

        self.btn_save_path = Button(self.btn_container, text="Salvar Path", width=12, command=self.save_path_click)
        self.btn_save_path.pack(side='left')

        self.btn_change_arqid = Button(self.btn_container, text="Alterar ArqID", width=12, command=self.change_arqid_click)
        self.btn_change_arqid.pack(side='right')

    def create_check_boxes(self, master=None): 
        self.chk_etrade = Checkbutton(master, text='Alterar do ETrade', variable=self.etrade_checked, onvalue = 1, offvalue = 0)
        self.chk_etrade["padx"] = 20
        self.chk_etrade.pack(side='left')

    def change_arqid_click(self):
        """Funcao do botao Alterar ArqID ao ser clicado"""
        self.mensagem['text'] = ''
        resultado = change_arqid.alterar_arqid(self.etrade_checked.get())
        self.mensagem['text'] = resultado
        importlib.reload(change_arqid) #gambiarra, descobrir outra forma de tratar isso

    def save_path_click(self):
        """Funcao para salvar os caminhos em um banco de dados"""
        path = self.path_repo.get()
        server = self.instance_server.get()
        station = self.instance_station.get()

        change_arqid.save_settings(path, server, station)

        self.mensagem['text'] = 'Informações salvas'
        importlib.reload(change_arqid)

    def load_paths(self):
        """Retorna os dados do banco para mostrar na tela"""
        row = change_arqid.get_settings()

        if row != None:
            self.path_repo.insert(0, row[1])
            self.instance_server.insert(0, row[2])
            self.instance_station.insert(0, row[3])
        
        self.mensagem['text'] = change_arqid.check_arqid_atual()
