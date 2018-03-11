"""Business Logic Layer da aplicacao """
import sqlite3

DB = sqlite3.connect('settings.db')
CURSOR = DB.cursor()

def save_data(path, server, station):
    """Salvando as configuracoes nos bancos de dados"""

    CURSOR.execute("SELECT * FROM settings")
    results = CURSOR.fetchone()
    if results is None:
        CURSOR.execute("INSERT INTO settings VALUES(1, '"+ path +"', '" +
                       server +"', '"+ station +"')")
    else:
        CURSOR.execute("UPDATE settings " +
                       "SET path = '" + path + "', instance_server = '" + server +
                       "', instance_station = '" + station + "'" +
                       "WHERE id = 1")

    DB.commit()

def get_data():
    """Pegando os dados no banco de dados"""
    CURSOR.execute("CREATE TABLE IF NOT EXISTS settings (id INTEGER, path TEXT, " +
                   "instance_server TEXT, instance_station TEXT)")

    CURSOR.execute("SELECT * FROM settings;")
    return CURSOR.fetchone()
