"""Executar a aplicacao change_arqid"""
from tkinter import Tk
from templates.main_window import MainWindow

if __name__ == "__main__":
    APP = Tk()
    APP.title("Canivete Suiço")
    APP.iconbitmap('icone.ico')
    X = (APP.winfo_screenwidth() - APP.winfo_reqwidth()) / 2
    Y = (APP.winfo_screenheight() - APP.winfo_reqheight()) / 2
    APP.geometry("+%d+%d" % (X, Y))
    APP.resizable(0, 0)
    MainWindow(APP)
    APP.mainloop()
