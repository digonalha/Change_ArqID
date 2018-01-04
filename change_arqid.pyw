"""Editor de arqId"""
import fileinput
import sys
import ctypes

LOCAL = r"localhost\sql2014"
BRIDGE_TEST = r"localhost\sqltest"

FIRST_LINE = open(r'C:\Repositorios\ETrade\PDV\ArqID.txt', 'r').readline()

SYSTEMS = ['PDV', 'UpdateAutomatic']

def alterar_arqid():
    """funcao para alterar o arqid"""
    for app in SYSTEMS:
        arqid = r"C:\Repositorios\ETrade\%s\ArqID.txt" %(app)
        if LOCAL.rsplit('\\', 1)[-1] in FIRST_LINE:
            for line in fileinput.input(arqid, inplace=True):
                sys.stdout.write(line.replace(LOCAL, BRIDGE_TEST))

            txtbox = BRIDGE_TEST

        else:
            for line in fileinput.input(arqid, inplace=True):
                sys.stdout.write(line.replace(BRIDGE_TEST, LOCAL))

            txtbox = LOCAL

    result = 'ArqID alterado para: %s' %(txtbox)

    if __name__ == '__main__':
        ctypes.windll.user32.MessageBoxW(0, result, "change arqid", 0)
        return result

    return result

if __name__ == '__main__':
    alterar_arqid()
