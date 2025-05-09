import sqlite3
from shortener import Base62_encoder
from contextlib import contextmanager

DB_PATH = 'database.db'

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def insert_url(original_url):
    with get_db() as conn:
        cursor = conn.execute("""INSERT INTO urls (original_url) VALUES (?) RETURNING Id
                    """, (original_url,))
        row = cursor.fetchone()
        if row:
            id = row[0]
            short_code = Base62_encoder(id)
            conn.execute(
                "UPDATE urls SET short_code = ? WHERE Id = ?",
                (short_code, id)
            )
            return short_code

def get_url_by_short_code(short_code):
    with get_db() as conn:
        cursor = conn.execute(
            "SELECT original_url FROM urls WHERE short_code = ?",
            (short_code,)
        )        
        row = cursor.fetchone()
        if row:
            url = row[0]
            return url


def list_all_urls():
    with get_db() as conn:
        cursor = conn.execute("""SELECT * FROM urls""")
        for row in cursor:
            print(row)


