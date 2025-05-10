# init_db.py
#ai_assisted
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT,
    clicks INTEGER DEFAULT 0,
    original_url TEXT NOT NULL,
    created_at DATETIME
)
''')

connection.commit()
connection.close()
