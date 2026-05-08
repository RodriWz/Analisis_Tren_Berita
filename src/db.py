import sqlite3
from config.settings import DB_PATH

def save_data(news_list):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        source TEXT,
        link TEXT UNIQUE,
        tanggal TEXT,
        description TEXT,
        guid TEXT
    )
    """)

    inserted = 0

    for n in news_list:
        try:
            c.execute("""
            INSERT OR IGNORE INTO news 
            (title, source, link, tanggal, description, guid)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                n["title"],
                n["source"],
                n["link"],
                n["tanggal"],
                n["description"],
                n["guid"]
            ))

            if c.rowcount > 0:
                inserted += 1

        except Exception as e:
            print("DB Error:", e)

    conn.commit()
    conn.close()

    return inserted