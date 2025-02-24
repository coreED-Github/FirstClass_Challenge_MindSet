import sqlite3

# Function to create database & table if not exists
def create_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS user_challenges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            date TEXT,
            challenge TEXT,
            reflection TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_challenge(email, date, challenge, reflection=""):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO user_challenges (email, date, challenge, reflection) VALUES (?, ?, ?, ?)", 
              (email, date, challenge, reflection))
    conn.commit()
    conn.close()


def get_user_challenges(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT date, challenge, reflection FROM user_challenges WHERE email = ?", (email,))
    data = c.fetchall()
    conn.close()
    return data

def delete_reflection(email, date, challenge):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("DELETE FROM user_challenges WHERE email = ? AND date = ? AND challenge = ?", (email, date, challenge))
    conn.commit()
    conn.close()