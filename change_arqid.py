"""Editor de arqId"""
import fileinput
import sys

LOCAL = r"localhost\sql2014"
BRIDGE_TEST = r"localhost\sqltest"

FIRST_LINE = open(r'C:\Repositorios\ETrade\PDV\ArqID.txt', 'r').readline()

SYSTEMS = ['PDV', 'UpdateAutomatic']

for app in SYSTEMS:
    arqid = r"C:\Repositorios\ETrade\%s\ArqID.txt" %(app)
    if LOCAL.rsplit('\\', 1)[-1] in FIRST_LINE:
        for line in fileinput.input(arqid, inplace=True):
            sys.stdout.write(line.replace(LOCAL, BRIDGE_TEST))
    else:
        for line in fileinput.input(arqid, inplace=True):
            sys.stdout.write(line.replace(BRIDGE_TEST, LOCAL))
        