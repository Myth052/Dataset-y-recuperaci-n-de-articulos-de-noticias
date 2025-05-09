import feedparser
import requests
from bs4 import BeautifulSoup

url = 'https://www.informador.mx/rss/mexico.xml'
feed = feedparser.parse(url)

for entry in feed.entries:
    title = entry.title
    summary_html = entry.summary  # 'summary' contiene el resumen en HTML

    # Limpiar el resumen usando BeautifulSoup para eliminar las etiquetas HTML
    soup = BeautifulSoup(summary_html, 'html.parser')
    summary_text = soup.get_text(separator=' ', strip=True)  # Obtener solo el texto y limpiar espacios en blanco

    # Si el resumen consiste solo en un enlace, intentar extraer el texto del enlace
    if summary_text.lower() == 'leer':
        response = requests.get(entry.link)
        link_soup = BeautifulSoup(response.content, 'html.parser')
        summary_text = link_soup.get_text(separator=' ', strip=True)

    # Truncar el resumen hasta el primer punto del texto
    summary_text = summary_text.split('.')[0] + '.'

    link = entry.link  # 'link' contiene el enlace directo

    print(f"Title: {title}\n\nSummary: {summary_text}\n\nLink: {link}\n\n--------------------------\n\n")
