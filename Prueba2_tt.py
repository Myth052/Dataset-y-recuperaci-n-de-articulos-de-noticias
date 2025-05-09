from bs4 import BeautifulSoup
import requests

# Lista de URLs de feeds RSS
urls = [
    'https://vanguardia.com.mx/rss.xml', #(Contaminado)
    #'https://e00-expansion.uecdn.es/rss/portada.xml',  # (Contaminado)
    # 'https://www.jornada.com.mx/rss/edicion.xml?v=1', # Aprobado
    # 'https://diario.mx/jrz/media/sitemaps/rss.xml', (Resumenes pobres)

    # 'https://www.reforma.com/rss/portada.xml' # (Aprobado en la versión 3)
]

for rss_url in urls:
    # Realiza una solicitud GET a la URL del feed RSS
    url = requests.get(rss_url)

    # Especifica 'lxml' como el analizador
    soup = BeautifulSoup(url.content, 'xml')

    # Corrige los nombres de las etiquetas a 'item'
    items = soup.find_all('item')
    i = 0
    for item in items:
        pub_date = item.pubDate.text  # Extrae la fecha del feed RSS
        title = item.title.text
        summary = item.description.text  # 'description' contiene el resumen
        link = item.link.text  # 'link' contiene el enlace directo
        i = i+1
        print(f"Documento {i}\n")
        # Imprime la fecha arriba del título
        print(f"URL del feed RSS: {rss_url}")
        print(f"Fecha: {pub_date}")
        print(f"Título: {title}\n\nResumen: {summary}\n\nLink: {link}\n\n--------------------------\n\n")
