"""Conexão com o banco"""
import sqlite3

DB = sqlite3.connect('settings.db')
CURSOR = DB.cursor()


def save_data(origem, destino):
    """Salvando as configuracoes nos bancos de dados"""

    CURSOR.execute("SELECT * FROM backup")
    results = CURSOR.fetchone()
    if results is None:
        CURSOR.execute("INSERT INTO backup VALUES(1, '" +
                       origem + "', '" + destino + "')")
    else:
        CURSOR.execute("UPDATE backup " +
                       "SET origem = '" + origem + "', destino = '" +
                       destino + "' WHERE id = 1")

    DB.commit()


def get_data():
    """Pegando os dados no banco de dados"""
    CURSOR.execute("CREATE TABLE IF NOT EXISTS backup " +
                   "(id INTEGER, origem TEXT, " +
                   "destino TEXT)")

    CURSOR.execute("SELECT * FROM backup;")
    return CURSOR.fetchone()
