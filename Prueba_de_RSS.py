import feedparser
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.elfinanciero.com.mx/arc/outboundfeeds/rss/?outputType=xml',
    'https://www.reforma.com/rss/portada.xml',
    'https://www.jornada.com.mx/rss/edicion.xml?v=1',
    'https://www.informador.mx/rss/mexico.xml',
    'https://www.vanguardia.com.mx/rss.xml',
]


documento_numero = 1
with open('DataSet_Feb_21.txt', 'w', encoding='utf-8') as archivo_txt:

    for url in urls:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            if 'published' in entry:
                news_date = entry.published
            elif 'updated' in entry:
                news_date = entry.updated
            else:
                news_date = 'Fecha no disponible'

            title = entry.title
            summary_html = entry.summary

            soup = BeautifulSoup(summary_html, 'html.parser')
            summary_text = soup.get_text(separator=' ', strip=True)

            if summary_text.lower() == 'leer':
                response = requests.get(entry.link)
                link_soup = BeautifulSoup(response.content, 'html.parser')
                summary_text = link_soup.get_text(separator=' ', strip=True)

            summary_text = summary_text.split('.')[0] + '.'

            link = entry.link

            archivo_txt.write(
                f"Documento {documento_numero}\nFecha: {news_date}\nTitle: {title}\nSummary: {summary_text}\nLink: {link}\n\n--------------------------\n\n")

            documento_numero += 1

print("Información guardada en DataSet_Feb_21.txt")
