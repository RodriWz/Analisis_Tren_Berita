from datetime import datetime
from src.rss import get_rss
from src.db import save_data

def run_job():
    print("=" * 50)
    print("Waktu:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    data = get_rss()
    print("Total diambil:", len(data))

    inserted = save_data(data)
    print("✔ Data masuk:", inserted)
    print("⚠ Duplikat:", len(data) - inserted)

    print("=" * 50)

if __name__ == "__main__":
    run_job()