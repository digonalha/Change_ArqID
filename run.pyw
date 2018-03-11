
"""Executar a aplicacao change_arqid"""
from tkinter import Tk
from templates.main_window import CreateInterface

if __name__ == "__main__":
    APP = Tk()
    APP.title("Change ArqID - v0.1")
    X = (APP.winfo_screenwidth() - APP.winfo_reqwidth()) / 2
    Y = (APP.winfo_screenheight() - APP.winfo_reqheight()) / 2
    APP.geometry("+%d+%d" % (X, Y))
    APP.resizable(0, 0)
    CreateInterface(APP)
    APP.mainloop()
