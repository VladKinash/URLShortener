# init_db.py
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT,
    original_url TEXT NOT NULL,
    created_at DATETIME
)
''')

cursor.execute("INSERT INTO urls (original_url) VALUES ('test.com'), ('test.com')")
connection.commit()
connection.close()
