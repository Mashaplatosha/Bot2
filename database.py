import sqlite3
from config import DB_NAME

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL,
            phone_number TEXT NOT NULL,
            registration_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            alert_time DATETIME,
            location TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
