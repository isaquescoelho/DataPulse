import sqlite3
import random

def setup_database(conn):
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT COUNT(*) FROM users')
        return True
    except sqlite3.OperationalError:
        return False

def insert_sample_data(conn):
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM users')
    current_users = cursor.fetchone()[0]

    users_to_add = 100000 - current_users

    for _ in range(users_to_add):
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('User', random.randint(18, 90)))

    conn.commit()
    cursor.close()
