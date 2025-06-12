# Modulos nativos
import time
from colorama import Fore as F
from colorama import init

# Modulos propios
from funcs.exts_list import exts

init(autoreset=True)

# ---------| Variables globales
color = ""
icon = ""


# =============================================================================
# Imprime el arbol de directorios con un formato legible, colores e iconos
# =============================================================================
def show_tree(tree, level=0, prefix=""):
    global color, icon

    keys = list(tree.keys())

    for i, (key, value) in enumerate(tree.items()):
        is_file = key.split("?")[0].endswith(tuple(f".{ext}" for ext in exts))
        is_last = (i == len(keys) - 1)

        color = F.RED if is_file else F.GREEN
        icon = "📄" if is_file else "📁"
        connector = "└──" if is_last else "├──"

        time.sleep(0.1)
        print(f"{prefix}{F.YELLOW}{connector} {color}{icon} {key}")

        if isinstance(value, dict):
            new_prefix = prefix + ("    " if is_last else f"{F.YELLOW}│   ")
            show_tree(value, level + 1, new_prefix)



# =============================================================================
# Imprime una lista de todas las URLs directas a los archivos y carpetas encontrados
# =============================================================================
def show_path(links, url):
    links_files_list = []

    for link in links:
        if link.startswith('#'):
            continue

        path_parts = link.strip('/').split('/')
        result = ""

        for part in path_parts:
            if part.endswith(tuple(f".{ext}" for ext in exts)):
                result += part
            else:
                result += f"{part}/"

        links_files_list.append(f"{url}/{result}")

    return links_files_list

