#no_ai
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

#original no-ai
#def list_all_urls():
#    with get_db() as conn:
#       cursor = conn.execute("""SELECT * FROM urls""")
#       return cursor.fetchall()


#fixed by ai
def list_all_urls():
    with get_db() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute("SELECT * FROM urls")
        return cursor.fetchall()



def increment_clicks(short_code):
    with get_db() as conn:
        conn.execute(
            "UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?",
            (short_code,)
        )

