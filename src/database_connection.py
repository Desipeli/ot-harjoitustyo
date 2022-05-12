import sqlite3


conn = sqlite3.connect("src/db.sqlite")


def get_conn():
    return conn
