"""Editor de arqId"""
import fileinput
import sys
import ctypes

LOCAL = r"localhost\sql2014"
BRIDGE_TEST = r"localhost\sqltest"

FIRST_LINE = open(r'C:\Users\usuario\Documents\ETrade\PDV\bin\Debug\ArqID.txt', 'r').readline()

SYSTEMS = ['PDV', 'UpdateAutomatic']

for app in SYSTEMS:
    arqid = r"C:\Users\usuario\Documents\ETrade\%s\bin\Debug\ArqID.txt" %(app)
    if LOCAL.rsplit('\\', 1)[-1] in FIRST_LINE:
        for line in fileinput.input(arqid, inplace=True):
            sys.stdout.write(line.replace(LOCAL, BRIDGE_TEST))
            
        txtbox = BRIDGE_TEST
        
    else:
        for line in fileinput.input(arqid, inplace=True):
            sys.stdout.write(line.replace(BRIDGE_TEST, LOCAL))
            
        txtbox = LOCAL

ctypes.windll.user32.MessageBoxW(0, 'ArqID alterado para: %s' %(txtbox), "Finalizado", 0)
        
