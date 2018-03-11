"""Editor de arqId"""
import fileinput
import sys
import ctypes
import db

sys.path.append("..")

SYSTEMS = ['PDV', 'UpdateAutomatic']

REMAIND_TEXT = "sa\nsenha\n30"

def save_settings(path, server, station):
    """Salva os novos caminhos no banco de dados"""
    db.save_data(path, server, station)

def get_settings():
    """Salva os novos caminhos no banco de dados"""
    return db.get_data()

def check_arqid_atual():
    try:
        row = get_settings()

        if row != None:
            path_repo = fix_path(row[1])
            check_this_file = open(path_repo + r'\PDV\bin\Debug\ArqID.txt', 'r').readline()           
            server = row[2]
            station = row[3]
        else:
            return "Os caminhos nao foram encontrados no banco de dados"

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

def alterar_arqid(alterar_etrade):
    """funcao para alterar o arqid"""
    try:
        row = get_settings()

        if row != None:
            path_repo = fix_path(row[1])
            check_this_file = open(path_repo + r'\PDV\bin\Debug\ArqID.txt', 'r').readline()         
            server = row[2]
            station = row[3]
        else:
            return "Os caminhos nao foram encontrados no banco de dados"

        if alterar_etrade == 1:
            SYSTEMS.append("ETrade")

        for app in SYSTEMS:
            arqid = path_repo + r"%s\bin\Debug\ArqID.txt" %(app)
            if server.rsplit('\\', 1)[-1] in check_this_file:
                for line in fileinput.input(arqid, inplace=True):
                    sys.stdout.write(line.replace(server, station))

                txtbox = station
            else:
                for line in fileinput.input(arqid, inplace=True):
                    sys.stdout.write(line.replace(station, server))

                txtbox = server
        result = '%s' %(txtbox)

        if __name__ == '__main__':
            ctypes.windll.user32.MessageBoxW(0, result, "change arqid", 0)
            return result

        return result
    except:
        return 'Verifique o caminho do repositório!'
    
if __name__ == '__main__':
    alterar_arqid(0)
