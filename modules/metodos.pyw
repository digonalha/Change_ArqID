"""Editor de arqId"""
import fileinput
import sys
import ctypes
import shutil
import db


sys.path.append("..")

SYSTEMS = ['PDV', 'UpdateAutomatic']


def save_settings(path, server, station):
    """Salva os novos caminhos no banco de dados"""
    db.save_data(path, server, station)


def get_settings():
    """Salva os novos caminhos no banco de dados"""
    return db.get_data()


def check_arqid_atual():
    try:
        row = get_settings()

        if row is not None:
            check_this_file = open(fix_path(row[1]) +
                                   r'\PDV\bin\Debug\ArqID.txt', 'r').readline()
            server = row[2]
            station = row[3]
        else:
            return "Os caminhos não foram encontrados no banco de dados"

        if server.rsplit('\\', 1)[-1] in check_this_file:
            return server
        else:
            return station
    except:
        return 'Verifique o caminho do repositório!'


def fix_path(caminho: str):
    if caminho.endswith('\\'):
        return caminho
    else:
        return caminho + '\\'


def change_line_on_file(arqid: str, instancia: str):
    from_file = open(arqid)
    line = from_file.readline()

    line = instancia + '\n'

    to_file = open(arqid, mode="w")
    to_file.write(line)
    shutil.copyfileobj(from_file, to_file)


def alterar_arqid(alterar_etrade: int, alterar_gourmet: int):
    """funcao para alterar o arqid"""
    try:
        row = get_settings()

        if row is not None:
            check_this_file = open(fix_path(row[1]) +
                                   r'\PDV\bin\Debug\ArqID.txt', 'r').readline()
            server = row[2]
            station = row[3]
        else:
            return "Os caminhos não foram encontrados no banco de dados"

        if alterar_etrade == 1:
            SYSTEMS.append("ETrade")
        if alterar_gourmet == 1:
            SYSTEMS.append("Gourmet")

        for app in SYSTEMS:
            arqid = fix_path(row[1]) + r"%s\bin\Debug\ArqID.txt" % (app)
            if server.rsplit('\\', 1)[-1] in check_this_file:
                change_line_on_file(arqid, station)
                result = station
            else:
                change_line_on_file(arqid, server)
                result = server

        if __name__ == '__main__':
            ctypes.windll.user32.MessageBoxW(0, result, "change arqid", 0)
            return result

        return result
    except:
        return 'Verifique o caminho do repositório!'


if __name__ == '__main__':
    alterar_arqid(0, 0)
