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

# Function to insert user challenge
def save_challenge(email, date, challenge, reflection=""):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO user_challenges (email, date, challenge, reflection) VALUES (?, ?, ?, ?)", 
              (email, date, challenge, reflection))
    conn.commit()
    conn.close()

# Function to fetch all previous challenges of a user
def get_user_challenges(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT date, challenge, reflection FROM user_challenges WHERE email = ?", (email,))
    data = c.fetchall()
    conn.close()
    return data

# ✅ Fixed: Corrected database name & table name in delete function
def delete_challenge(date, email):
    conn = sqlite3.connect("data.db")  # Fixed: Using "data.db" instead of "challenges.db"
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_challenges WHERE date = ? AND email = ?", (date, email))  # Fixed: Correct table name
    conn.commit()
    conn.close()