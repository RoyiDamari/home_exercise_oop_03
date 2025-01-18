import sqlite3

conn: any = None
cursor: any = None

def connection(file: str) -> None:
    global conn, cursor
    conn = sqlite3.connect(file)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

def run_query_select(query: str) -> list[tuple]:
    cursor.execute(query)
    columns = cursor.fetchall()
    return columns

def run_query_update(query: str, params: tuple = ()) -> None:
    cursor.execute(query, params)
    cursor.connection.commit()

def close():
    cursor.close()