import sqlite3


conn = sqlite3.connect("src/db.sqlite")
#conn.row_factory = sqlite3.Row

def get_conn():
    return conn
