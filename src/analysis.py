import sqlite3
from collections import Counter
from config.settings import *
from src.utils import clean_text, filter_short_words

# ambil data
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("SELECT title FROM news WHERE title IS NOT NULL")
titles = [r[0] for r in c.fetchall()]

# cleaning
cleaned = [clean_text(t) for t in titles]

# auto stopword
all_words = " ".join(cleaned).split()
word_count = Counter(all_words)

auto_stopwords = set([
    w for w, c in word_count.most_common(AUTO_STOPWORD_TOP_N)
])

# manual stopword tambahan
manual_stopwords = {
    "cnn","detik","kompas","tribun","news",
    "indonesia","jakarta","video","update"
}

stopwords = auto_stopwords.union(manual_stopwords)

# remove stopwords
filtered = [
    " ".join([w for w in t.split() if w not in stopwords])
    for t in cleaned
]

# filter kata pendek
filtered = [filter_short_words(t, MIN_WORD_LENGTH) for t in filtered]

# hitung keyword
words = " ".join(filtered).split()
counts = Counter(words)

final = {
    k:v for k,v in counts.items()
    if v >= MIN_FREQ
}

top = sorted(final.items(), key=lambda x: x[1], reverse=True)[:10]

print("\n=== TOP KEYWORD FINAL ===")
for w,c in top:
    print(w, ":", c)

# simpan
with open("data/hasil_keyword_final.txt", "w") as f:
    for w,c in top:
        f.write(f"{w}:{c}\n")