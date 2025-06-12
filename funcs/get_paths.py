"""
Se conecta a una URL, obtiene su HTML, y extrae todos los valores de los atributos 
href y src de etiquetas como <a>, <img>, <script>, <link> e <iframe>, devolviendo 
una lista limpia de URLs encontradas.
"""

import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import unquote


# ----------| Desactivar advertencia de certificados SSL inseguros
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# =============================================================================
# Obtiene el codigo HTML y busca argumentos href y src en las etiquetas para posteriormente agruparlos en una lista
# =============================================================================
def get_url(url):
    urls_found = []

    response = requests.get(url, verify=False, allow_redirects=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        tags_with_href = soup.find_all(["a", "img", "script", "link"], href=True)
        tags_with_src  = soup.find_all(["img", "script", "iframe"], src=True)


        for tag in tags_with_href:
            raw_url = tag["href"]
            clean_url = unquote(raw_url).strip().replace(",", "")
            urls_found.append(clean_url)

        for tag in tags_with_src:
            raw_url = tag["src"]
            clean_url = unquote(raw_url).strip().replace(",", "")
            urls_found.append(clean_url)

    else:
        print(f"Error code: {response.status_code}")

    return urls_found
