"""BLL para alterção do ArqID"""
import fileinput
import sys
import os
import ctypes
import shutil
import win32serviceutil
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


def make_backup():
    row = get_settings()

    if row is not None:
        origem = fix_path(row[1])
        destino = fix_path(row[2])
    else:
        return "Os caminhos não foram encontrados no banco de dados"

    bd = origem + 'Etrade.mdf'
    log = origem + 'Etrade_log.ldf'

    win32serviceutil.StopService('Elan Service')
    shutil.copy2(bd, destino)
    shutil.copy2(log, destino)
    # win32serviceutil.StartService('Elan Service')

    return 'Backup restaurado!'


def get_status_service():
    if win32serviceutil.QueryServiceStatus('Elan Service')[1] == 4:
        return "O serviço esta em execução"        
    else:
        return "O serviço está parado"

