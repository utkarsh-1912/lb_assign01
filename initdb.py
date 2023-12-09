import sqlite3

def init_db():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY, title TEXT, author TEXT, published_year INTEGER)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

