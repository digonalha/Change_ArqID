"""Tela da aplicaçao de alteracao de arqid"""
import importlib
import sys
from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Label, ttk
from modules import metodos

sys.path.append("..")


class MainWindow:
    """Montando a tela"""
    # pylint: disable=too-many-instance-attributes

    def __init__(self, master=None):

        self.etrade_checked = IntVar()
        self.gourmet_checked = IntVar()
        self.n = ttk.Notebook(master)
        self.default_font = ("Segoe", "11")
        self.font_input = ("Arial", "10")
        self.create_tab_changearqid(master)
        self.create_tab_backupbanco(master)
        self.n.pack()

    def create_tab_changearqid(self, master=None):
        f1 = Frame(self.n)
        self.n.add(f1, text='Alterar ArqID')
        self.create_title("Alterar instância no ArqID", f1)
        self.create_frames_arqid(f1)
        self.create_check_boxes(f1)
        self.create_buttons(f1)
        self.load_paths()

    def create_tab_backupbanco(self, master=None):
        f2 = Frame(self.n)
        self.n.add(f2, text='Backup Banco')
        self.create_title("Backup do banco de dados", f2)
        self.create_frames_backup(f2)

# region Comum

    def create_title(self, title: str, master=None):
        """Criando o titulo da aplicacao"""
        self.lbl_titulo = Frame(master)
        self.lbl_titulo["pady"] = 10
        self.lbl_titulo.pack()
        self.titulo = Label(self.lbl_titulo, text=title)
        self.titulo["font"] = ("Arial", "11", "bold")
        self.titulo.pack()

# endregion

# region Alterar ArqID

    def create_frames_arqid(self, master=None):
        """Criando os frames(txtedits) da aplicacao"""

        # --------------------REPOSITORIO-----------------

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

        # ---------------------SERVIDOR-----------------

        self.txt_server = Frame(master)
        self.txt_server["padx"] = 20
        self.txt_server.pack()

        self.new_label = Label(self.txt_server, text="Servidor     ",
                               font=self.default_font)
        self.new_label.pack(side='left')

        self.instance_server = Entry(self.txt_server)
        self.instance_server["width"] = 45
        self.instance_server["font"] = self.font_input
        self.instance_server.pack(side='left')

        # ----------------------ESTAÇÃO------------------

        self.txt_station = Frame(master)
        self.txt_station["padx"] = 20
        self.txt_station.pack()

        self.new_label = Label(self.txt_station, text="Estação     ",
                               font=self.default_font)
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

        self.txt_status = Label(self.txt_container,
                                text="Instância atual")
        self.txt_status["font"] = ("Arial", "9", "bold")
        self.txt_status.pack(side='top')

        self.mensagem = Label(self.txt_container,
                              text="",
                              foreground="green")
        self.mensagem["font"] = ("Arial", "9", "bold")
        self.mensagem.pack(anchor="center")

        self.btn_save_path = Button(self.btn_container,
                                    text="Salvar Path",
                                    width=12,
                                    command=self.save_path_click)
        self.btn_save_path.pack(side='left')

        self.btn_change_arqid = Button(self.btn_container,
                                       text="Alterar ArqID",
                                       width=12,
                                       command=self.change_arqid_click)
        self.btn_change_arqid.pack(side='right')

    def create_check_boxes(self, master=None):
        self.chk_container = Frame(master)
        self.chk_container.pack()

        self.chk_etrade = Checkbutton(self.chk_container,
                                      text='Alterar no ETrade',
                                      variable=self.etrade_checked,
                                      onvalue=1,
                                      offvalue=0)
        self.chk_etrade["padx"] = 5
        self.chk_etrade.pack(side='left')
        self.chk_gourmet = Checkbutton(self.chk_container,
                                       text='Alterar no Gourmet',
                                       variable=self.gourmet_checked,
                                       onvalue=1,
                                       offvalue=0)
        self.chk_gourmet["padx"] = 20
        self.chk_gourmet.pack(side='right')

    def change_arqid_click(self):
        """Funcao do botao Alterar ArqID ao ser clicado"""
        self.mensagem['text'] = ''
        resultado = metodos.alterar_arqid(
                    alterar_etrade=self.etrade_checked.get(),
                    alterar_gourmet=self.gourmet_checked.get())
        self.mensagem['text'] = resultado

        self.refresh_msg_color(resultado)
        # gambiarra, descobrir# outra forma de tratar isso
        importlib.reload(metodos)

    def save_path_click(self):
        """Funcao para salvar os caminhos em um banco de dados"""
        path = self.path_repo.get()
        server = self.instance_server.get()
        station = self.instance_station.get()

        metodos.save_settings(path, server, station)

        self.mensagem['text'] = 'Informações salvas'
        self.mensagem["foreground"] = "red"
        importlib.reload(metodos)

    def load_paths(self):
        """Retorna os dados do banco para mostrar na tela"""
        row = metodos.get_settings()

        if row is not None:
            self.path_repo.insert(0, row[1])
            self.instance_server.insert(0, row[2])
            self.instance_station.insert(0, row[3])

        resultado = metodos.check_arqid_atual()
        self.mensagem['text'] = resultado
        self.refresh_msg_color(resultado)

    def refresh_msg_color(self, result: str):
        if 'Verifique' in result:
            self.mensagem["foreground"] = "red"
        elif 'Os caminhos' in result:
            self.mensagem["foreground"] = "red"
        else:
            self.mensagem["foreground"] = "green"

# endregion

# region Backup Banco
    def create_frames_backup(self, master=None):
        """Criando os frames(txtedits) da aplicacao"""

        self.txt_origem = Frame(master)
        self.txt_origem["padx"] = 20
        self.txt_origem.pack()

        self.new_label = Label(self.txt_origem, text="Origem     ",
                               font=self.default_font)
        self.new_label.pack(side='left')

        self.path_origem = Entry(self.txt_origem)
        self.path_origem["width"] = 45
        self.path_origem["font"] = self.font_input
        self.path_origem.pack(side='left')

        self.txt_destino = Frame(master)
        self.txt_destino["padx"] = 20
        self.txt_destino.pack()

        self.new_label = Label(self.txt_destino, text="Destino    ",
                               font=self.default_font)
        self.new_label.pack(side='left')

        self.path_destino = Entry(self.txt_destino)
        self.path_destino["width"] = 45
        self.path_destino["font"] = self.font_input
        self.path_destino.pack(side='left')
# endregion
