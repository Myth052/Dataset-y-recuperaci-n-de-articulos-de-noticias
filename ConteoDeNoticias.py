import xml.etree.ElementTree as ET

archivo_xml = "noticias_clasificadas.xml"

conteo_categorias = {
    "políticas": 0,
    "deportivas": 0,
    "económicas": 0,
    "culturales": 0,
    "sociales": 0,
    "de_farándula": 0,
    "policiales": 0,
    "científicas": 0,
    "No clasificada": 0
}

tree = ET.parse(archivo_xml)
root = tree.getroot()
conteo_selecto = 0
for noticia in root.findall('noticia'):

    categoria = noticia.get('categoria')
    conteo_categorias[categoria] += 1
    if categoria != "No clasificada":
        conteo_selecto += 1



print("Conteo de noticias por categoría:")
for categoria, conteo in conteo_categorias.items():
    print(f"{categoria}: {conteo}")

print(f"El numero total de noticias clasificadas con exito es de: {conteo_selecto} noticias")

