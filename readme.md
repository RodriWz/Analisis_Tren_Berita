# 📰 Analisis Berita Indonesia: Sentimen & Tren Topik Berbasis Big Data

## 📌 Deskripsi

Project ini merupakan implementasi **Big Data Pipeline** untuk menganalisis berita Indonesia yang diambil dari NewsAPI. Pipeline mencakup proses:

- **Data Ingestion** — Pengambilan data berita via NewsAPI
- **Data Storage** — Penyimpanan ke database SQLite
- **Data Preprocessing** — Pembersihan teks (HTML cleaning, stopword removal, stemming)
- **Data Analysis** — Analisis sentimen & topic modeling (LDA)
- **Data Visualization** — Visualisasi insight dari data berita

---

## 🎯 Tujuan Project

- Mengambil data berita berbahasa Indonesia dari NewsAPI
- Menyimpan data ke database secara terstruktur
- Membersihkan dan memproses teks berita
- Mengklasifikasikan berita berdasarkan sentimen (positif / negatif / netral)
- Menemukan topik dominan dari keseluruhan berita menggunakan LDA
- Menampilkan insight bisnis dari data berita Indonesia

---

## ⚙️ Teknologi yang Digunakan

| Kategori | Library / Tools |
|---|---|
| Bahasa | Python |
| Database | SQLite |
| Notebook | Jupyter Notebook |
| Manipulasi Data | Pandas |
| Pembersihan Teks | BeautifulSoup4, NLTK, Sastrawi |
| Analisis Sentimen | NLTK / IndoNLU |
| Topic Modeling | Gensim (LDA) |
| Visualisasi | Matplotlib, WordCloud |

---

## 📁 Struktur Project

```
big-data/
│
├── src/                        # Core logic program
│   ├── main.py                 # Entry point scraping
│   ├── rss.py                  # Scraping NewsAPI
│   ├── db.py                   # Database handler
│   └── utils.py                # Helper functions
│
├── config/                     # Konfigurasi
│   └── settings.py             # API Key, DB path, parameter
│
├── data/                       # Penyimpanan data
│   ├── news.db                 # Database SQLite (raw)
│   └── news_bersih.csv         # Data hasil preprocessing
│
├── notebooks/                  # Analisis data
│   ├── 01_eksplorasi.ipynb     # Eksplorasi & EDA
│   ├── 02_preprocessing.ipynb  # Cleaning & preprocessing teks
│   ├── 03_sentimen.ipynb       # Analisis sentimen
│   └── 04_topik_visualisasi.ipynb  # Topic modeling & visualisasi
│
├── venv/                       # Virtual environment
│
└── README.md
```

---

## 🔄 Alur Sistem

```
NewsAPI (lang=id)
       ↓
  Scraping Data
       ↓
  Simpan ke SQLite
       ↓
  Jupyter Notebook
       ↓
  ┌────────────────────┐
  │   Preprocessing    │
  │ - Bersihkan HTML   │
  │ - Hapus stopword   │
  │ - Stemming         │
  └────────────────────┘
       ↓
  ┌─────────────────────────────────────┐
  │            Analisis                 │
  │  Sentimen          Topic Modeling   │
  │ (pos/neg/netral)      (LDA)         │
  └─────────────────────────────────────┘
       ↓
  Visualisasi & Insight
```

---

## 🚀 Cara Menjalankan Project

### 1. Buat Virtual Environment

```bash
py -m venv venv
```

### 2. Aktifkan Venv

PowerShell:
```bash
.\venv\Scripts\activate
```

Git Bash:
```bash
source venv/Scripts/activate
```

### 3. Install Dependency

```bash
pip install pandas matplotlib beautifulsoup4 nltk sastrawi gensim wordcloud jupyter ipykernel
```

### 4. Jalankan Scraping

```bash
py -m src.main
```

### 5. Jalankan Jupyter Notebook

```bash
jupyter notebook
```

---

## 🧹 Preprocessing

Dilakukan di `02_preprocessing.ipynb` dengan tahap:

1. **HTML Cleaning** — Hapus tag HTML dari kolom description
2. **Lowercase** — Ubah semua teks ke huruf kecil
3. **Hapus simbol & angka** — Bersihkan karakter tidak relevan
4. **Stopword Removal** — Hapus kata umum bahasa Indonesia
5. **Stemming** — Ubah kata ke bentuk dasar (Sastrawi)

---

## 📊 Analisis Data

### Analisis Sentimen
- Mengklasifikasikan setiap berita menjadi: **Positif**, **Negatif**, atau **Netral**
- Melihat distribusi sentimen per topik dan per waktu

### Topic Modeling (LDA)
- Menemukan topik dominan dari 1705 berita
- Mengidentifikasi kata kunci utama tiap topik
- Melihat tren topik dari waktu ke waktu

---

## 📈 Visualisasi

- Bar chart distribusi sentimen
- Line chart tren berita per hari
- Word cloud kata dominan
- Grafik topik dominan per kategori

---

## 💡 Insight

Contoh insight yang dihasilkan:

> Berita Indonesia didominasi oleh topik **ekonomi dan geopolitik** dengan sentimen cenderung **negatif**, mencerminkan kekhawatiran publik terhadap isu harga dan keamanan.

---

## 🧱 Struktur Database

Tabel: `news`

| Kolom | Tipe | Keterangan |
|---|---|---|
| id | INTEGER | Primary key |
| title | TEXT | Judul berita |
| source | TEXT | Sumber media |
| link | TEXT | URL berita |
| tanggal | TEXT | Tanggal publikasi |
| description | TEXT | Ringkasan (format HTML) |
| guid | TEXT | ID unik dari NewsAPI |

---

## ⚠️ Catatan

- Data berjumlah **1705 berita** berbahasa Indonesia dari NewsAPI
- Sumber berita mencakup media Indonesia dan berita internasional berbahasa Indonesia
- Preprocessing menggunakan library khusus bahasa Indonesia (Sastrawi)

---

## 🔮 Pengembangan Selanjutnya

- Real-time pipeline menggunakan Apache Kafka
- Dashboard interaktif dengan Streamlit
- Analisis sentimen berbasis model IndoBERT
- Skalabilitas menggunakan Apache Spark

---

## 👨‍💻 Author

**Rohdrigues Lytonio**  
Project ini dibuat untuk keperluan tugas mata kuliah Big Data.