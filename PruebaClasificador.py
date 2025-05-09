import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def clasificar_noticias(texto):
    texto = texto.lower()

    categorias = {
        "políticas": ["política", "gobierno", "elecciones", "presidente", "congreso"],
        "deportivas": ["deporte", "equipo", "jugador", "partido", "campeonato"],
        "económicas": ["economía", "finanzas", "trabajo", "empresas", "mercado"],
        "culturales": ["cultura", "arte", "literatura", "música", "teatro"],
        "sociales": ["comunidad", "sociedad", "eventos", "ciudadanos", "solidaridad"],
        "de_farándula": ["espectáculo", "moda", "estrella", "cine", "televisión"],
        "policiales": ["policía", "crimen", "investigación", "delito", "seguridad"],
        "científicas": ["ciencia", "tecnología", "investigación", "descubrimiento", "innovación"]
    }

    for categoria, palabras_clave in categorias.items():
        for palabra in palabras_clave:
            if palabra in texto:
                return categoria

    return "No clasificada"


carpeta = "C:/Users/marco/PycharmProjects/Practica2/Pruebas_del_TT"
documento_numero = 1
root = ET.Element("noticias")

for filename in os.listdir(carpeta):
    if filename.endswith(".txt"):
        filepath = os.path.join(carpeta, filename)

        with open(filepath, 'r', encoding='utf-8') as archivo_txt:
            contenido = archivo_txt.read()
            noticias = contenido.split("\n\n--------------------------\n\n")

            for noticia in noticias:
                fecha = "Fecha no disponible"
                titulo = "Título no disponible"
                resumen = "Resumen no disponible"
                link = "Link no disponible"

                if "Fecha:" in noticia:
                    fecha = noticia.split("Fecha:")[1].split("\n")[0].strip()
                if "Title:" in noticia:
                    titulo = noticia.split("Title:")[1].split("\n")[0].strip()
                if "Summary:" in noticia:
                    resumen = noticia.split("Summary:")[1].split("\n")[0].strip()
                if "Link:" in noticia:
                    link = noticia.split("Link:")[1].split("\n")[0].strip()

                categoria = clasificar_noticias(noticia)

                news_item = ET.SubElement(root, "noticia")
                news_item.set("documento_numero", str(documento_numero))
                news_item.set("fecha", fecha)
                news_item.set("titulo", titulo)
                news_item.set("resumen", resumen)
                news_item.set("link", link)
                news_item.set("categoria", categoria)

                documento_numero += 1

tree = ET.ElementTree(root)
tree.write("noticias_clasificadas.xml")

print("Noticias clasificadas guardadas en noticias_clasificadas.xml")
