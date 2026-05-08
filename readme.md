# 📰 News Big Data Pipeline (RSS Scraping & Analysis)

## 📌 Deskripsi

Project ini merupakan implementasi sederhana konsep **Big Data Pipeline** yang mencakup proses:

* Data Ingestion (pengambilan data)
* Data Storage (penyimpanan)
* Data Preprocessing (pembersihan data)
* Data Analysis (analisis data)
* Data Visualization (visualisasi)

Data yang digunakan berasal dari berbagai sumber berita melalui RSS feed.

---

## 🧠 Tujuan Project

* Mengambil data berita dari berbagai sumber
* Menyimpan data ke database
* Membersihkan data teks
* Menganalisis tren keyword berita
* Menampilkan insight dari data

---

## ⚙️ Teknologi yang Digunakan

* Python
* SQLite
* Jupyter Notebook
* Pandas
* Matplotlib
* Feedparser

---

## 📁 Struktur Project

```
big-data/
│
├── src/                # Core logic program
│   ├── main.py         # Entry point
│   ├── rss.py          # Scraping RSS
│   ├── db.py           # Database handler
│   └── utils.py        # Helper functions
│
├── config/             # Konfigurasi
│   └── settings.py     # RSS URL & DB path
│
├── data/               # Penyimpanan data
│   └── news.db         # Database SQLite
│
├── notebooks/          # Analisis data
│   └── analysis.ipynb  # Cleaning & visualisasi
│
├── venv/               # Virtual environment
│
└── README.md
```

---

## 🔄 Alur Sistem

```
RSS Feed
   ↓
Scraping (rss.py)
   ↓
Processing Data
   ↓
Database (SQLite)
   ↓
Jupyter Notebook
   ↓
Cleaning & Analysis
   ↓
Visualization & Insight
```

---

## 🚀 Cara Menjalankan Project

### 1. Buat Virtual Environment

```
py -m venv venv
```

### 2. Aktifkan Venv

* PowerShell:

```
.\venv\Scripts\activate
```

* Git Bash:

```
source venv/Scripts/activate
```

---

### 3. Install Dependency

```
pip install pandas matplotlib feedparser jupyter ipykernel
```

---

### 4. Jalankan Scraping

```
py -m src.main
```

---

### 5. Jalankan Jupyter Notebook

```
jupyter notebook
```

Pilih kernel:

```
Python (bigdata-venv)
```

---

## 🧹 Data Cleaning

Dilakukan di Jupyter Notebook dengan tahap:

* Lowercase
* Menghapus simbol & angka
* Stopword removal
* Filtering kata penting

---

## 📊 Analisis Data

* Menghitung frekuensi kata (keyword)
* Menentukan topik dominan
* Visualisasi menggunakan bar chart

---

## 💡 Insight

Contoh insight:

> Topik berita didominasi oleh isu geopolitik dan ekonomi berdasarkan frekuensi kata yang muncul.

---

## 🧱 Struktur Database

Tabel: `news`

| Kolom       | Tipe    | Keterangan     |
| ----------- | ------- | -------------- |
| id          | INTEGER | Primary key    |
| title       | TEXT    | Judul berita   |
| source      | TEXT    | Sumber berita  |
| link        | TEXT    | URL (unik)     |
| tanggal     | TEXT    | Tanggal berita |
| description | TEXT    | Ringkasan      |
| guid        | TEXT    | ID dari RSS    |

---

## ⚠️ Catatan

* Data masih dalam skala kecil (simulasi Big Data)
* Sistem dapat dikembangkan untuk skala lebih besar
* Beberapa sumber RSS mungkin memblok request

---

## 🔮 Pengembangan Selanjutnya

* Menggunakan Apache Spark untuk data besar
* Menambahkan dashboard (Power BI / Streamlit)
* Analisis sentimen
* Real-time data pipeline

---

## 👨‍💻 Author

Project ini dibuat untuk keperluan pembelajaran Big Data.

---
