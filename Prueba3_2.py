import feedparser
from bs4 import BeautifulSoup

# Lista de URLs de los feeds RSS que deseas recuperar
urls = [
    'https://www.elfinanciero.com.mx/arc/outboundfeeds/rss/?outputType=xml',
    'https://www.reforma.com/rss/portada.xml',
    'https://www.jornada.com.mx/rss/edicion.xml?v=1'
    # Agrega más URLs según sea necesario
]

# Inicializar el contador
documento_numero = 1

# Recorrer la lista de URLs
for url in urls:
    feed = feedparser.parse(url)

    # Recorrer las entradas del feed RSS
    for entry in feed.entries:
        # Obtener la fecha de la noticia
        if 'published' in entry:
            news_date = entry.published
        elif 'updated' in entry:
            news_date = entry.updated
        else:
            news_date = 'Fecha no disponible'

        title = entry.title
        summary_html = entry.summary  # 'summary' contiene el resumen en HTML

        # Limpiar el resumen usando BeautifulSoup para eliminar las etiquetas HTML
        soup = BeautifulSoup(summary_html, 'html.parser')
        summary_text = soup.get_text(separator=' ', strip=True)  # Obtener solo el texto y limpiar espacios en blanco

        link = entry.link  # 'link' contiene el enlace directo

        # Mostrar el número de documento y el resto de la información
        print(
            f"Documento {documento_numero}\nFecha: {news_date}\nTitle: {title}\nSummary: {summary_text}\nLink: {link}\n\n--------------------------\n\n")

        # Incrementar el contador de documentos
        documento_numero += 1
