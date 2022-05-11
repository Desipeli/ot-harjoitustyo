from database_connection import get_conn


def drop_tables(conn):
    """ Delete tables if exists

        Args:
            conn: Connection object of the database
    """

    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Wins
    """)
    conn.commit()

def create_tables(conn):
    """ Create tables for database

        Args:
            conn: Connection object of the database
    """

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Wins (id INTEGER PRIMARY KEY ,player_points INTEGER, computer_points INTEGER);
    """)

    conn.commit()

def initialize_database():
    conn = get_conn()

    drop_tables(conn)
    create_tables(conn)


if __name__ == "__main__":
    initialize_database()
