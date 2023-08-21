import random
import time
from multiprocessing import Pool
from src.database.connection import get_connection, close_connection
from src.database.operations import insert_sample_data

def fetch_data(_):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE age=?', (random.randint(18, 90),))
    data = cursor.fetchall()

    cursor.close()
    close_connection
    return data

def fetch_data_sequencial():
    conn = get_connection()
    cursor = conn.cursor()

    fetched_data = []
    for _ in range(4):
        cursor.execute('SELECT * FROM users WHERE age=?', (random.randint(18, 90),))
        data = cursor.fetchall()
        fetched_data.extend(data)

    cursor.close()
    close_connection(conn)
    return fetched_data

def print_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()

    for user in all_users:
        print(user)

    cursor.close()
    close_connection(conn)

if __name__ == "__main__":
    conn = get_connection()
    insert_sample_data(conn)
    close_connection(conn)

    with Pool(4) as p:
        start_time_parallel = time.time()
        result_parallel = p.map(fetch_data, [None] * 4)
        end_time_parallel = time.time()
        time_taken_parallel = end_time_parallel - start_time_parallel
        print(f'Parallel Fetch Time: {time_taken_parallel} seconds.')

    start_time_sequential = time.time()
    result_sequential = fetch_data_sequencial()
    end_time_sequential = time.time()
    time_taken_sequential = end_time_sequential - start_time_sequential
    print(f'Sequential Fetch Time: {time_taken_sequential} seconds.')

    if time_taken_parallel > time_taken_sequential:
        print('Parallel fetching was slower than sequential fetching.')
    elif time_taken_sequential > time_taken_parallel:
        print('Sequential fetching was slower than parallel fetching.')
    else:
        print('Both methods took the same amount of time.')
