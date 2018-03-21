"""BLL para alterção do ArqID"""
import fileinput
import sys
import os
import ctypes
import shutil
from DAL import backup_dal

sys.path.append("..")


def save_path_backup(origem, destino):
    """Salva os novos caminhos no banco de dados"""
    backup_dal.save_data(origem, destino)


def get_settings():
    """Salva os novos caminhos no banco de dados"""
    return backup_dal.get_data()


def fix_path(caminho: str):
    if caminho.endswith('\\'):
        return caminho
    else:
        return caminho + '\\'


def make_backup_as_admin():
    if is_admin():
        make_backup()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas",
                                            sys.executable, "", None, 1)
        make_backup()


def make_backup():
    row = get_settings()

    if row is not None:
        origem = fix_path(row[1])
        destino = fix_path(row[2])
    else:
        return "Os caminhos não foram encontrados no banco de dados"

    bd = origem + 'Etrade.mdf'
    log = origem + 'Etrade_log.ldf'

    toggle_service('MSSQL$SQL2014', 'stop')
    shutil.copy2(bd, destino)
    shutil.copy2(log, destino)
    toggle_service('MSSQL$SQL2014', 'start')

    return 'Backup restaurado!'


def toggle_service(name, action):
        cmd = 'runas /noprofile /user:administrator "net {} \'{}\'"'.format(action, name)
        os.system(cmd)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
