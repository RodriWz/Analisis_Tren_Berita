@echo off
TITLE News Big Data Scraper
echo ==================================================
echo       News Big Data Scraper (Otomatis)
echo ==================================================
echo.
echo Program ini akan mengambil data dari RSS setiap 1 jam.
echo JANGAN TUTUP jendela ini agar pengambilan tetap berjalan.
echo.
cd /d %~dp0
.\venv\Scripts\python.exe -m src.main
pause
