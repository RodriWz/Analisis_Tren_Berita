import feedparser
import urllib.request
from config.settings import RSS_URLS

def get_rss():
    news = []

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for url in RSS_URLS:
        try:
            feed = feedparser.parse(url)

            for entry in feed.entries:
                news.append({
                    "title": entry.title if "title" in entry else "",
                    "link": entry.link if "link" in entry else "",
                    "tanggal": entry.published if "published" in entry else "",
                    "description": entry.summary if "summary" in entry else "",
                    "source": entry.source.title if "source" in entry else url,
                    "guid": entry.id if "id" in entry else entry.link
                })

        except Exception as e:
            print("Error:", url, e)

    return news