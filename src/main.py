import time
from datetime import datetime
from src.rss import get_rss
from src.db import save_data

def run_job(continuous=True):
    while True:
        print("\n" + "=" * 50)
        print("Waktu:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        data = get_rss()
        print("Total diambil dari RSS:", len(data))

        inserted = save_data(data)
        print("DONE Data baru disimpan:", inserted)
        print("SKIP Duplikat (diabaikan):", len(data) - inserted)

        if not continuous:
            print("=" * 50)
            break
        
        print("\nMenunggu 1 jam untuk pengambilan berikutnya...")
        print("=" * 50)
        
        # Sleep selama 1 jam (3600 detik)
        time.sleep(3600)

if __name__ == "__main__":
    # Ubah continuous=False jika hanya ingin menjalankan 1 kali saja
    run_job(continuous=True)