import sqlite3

def get_connection():
    return sqlite3.connect('data/users.db')

def close_connection(conn):
    conn.close()
