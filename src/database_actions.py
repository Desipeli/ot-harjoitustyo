from database_connection import get_conn


def read_wins():
    try:
        conn = get_conn()
        cursor = conn.cursor()

        sql = "SELECT count(*) FROM Wins WHERE player_points > computer_points;"
        cursor.execute(sql)
        wins = cursor.fetchone()[0]
        sql = "SELECT count(*) FROM Wins;"
        cursor.execute(sql)
        all_games = cursor.fetchone()[0]
        return wins, all_games
    except Exception as e:
        print(e)
        return None

def update_wins(player_points, computer_points):
    try:
        conn = get_conn()
        cursor = conn.cursor()

        sql = "INSERT INTO Wins (player_points, computer_points) VALUES (?, ?);"
        cursor.execute(sql, (player_points, computer_points))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
