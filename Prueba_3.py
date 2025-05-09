import feedparser
from bs4 import BeautifulSoup

url = 'https://www.elfinanciero.com.mx/arc/outboundfeeds/rss/?outputType=xml'
feed = feedparser.parse(url)

for entry in feed.entries:
    title = entry.title
    summary_html = entry.summary  # 'summary' contiene el resumen en HTML

    # Limpiar el resumen usando BeautifulSoup para eliminar las etiquetas HTML
    soup = BeautifulSoup(summary_html, 'html.parser')
    summary_text = soup.get_text(separator=' ', strip=True)  # Obtener solo el texto y limpiar espacios en blanco

    link = entry.link  # 'link' contiene el enlace directo

    print(f"Title: {title}\n\nSummary: {summary_text}\n\nLink: {link}\n\n--------------------------\n\n")

