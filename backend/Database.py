import mysql.connector
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="abc123",
        database="echotrace"
    )

def log_event(attack_type, probability, action):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO logs (timestamp, attack_type, probability, action_taken)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (
        datetime.now(),
        attack_type,
        probability,
        action
    ))

    conn.commit()
    cursor.close()
    conn.close()
