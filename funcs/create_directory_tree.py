"""
Analiza una lista de rutas o URLs, separa las carpetas de los archivos, 
construye un árbol de directorios representando su estructura, y clasifica los archivos 
por extensión, contando cuántos hay de cada tipo y guardando sus nombres.
"""

all_files = {}

# ---------| Extenciones comunes 
exts = [
    "php", "asp", "aspx", "jsp", "cgi", "pl", "py", "rb",
    "js", "json", "xml",
    "env", "config", "ini", "yml", "yaml",
    "bak", "old", "zip", "rar",
    "log", "sql", "db",
    "htaccess", "htpasswd",
    "pem", "key", "crt", "p12", "pfx",
    "inc", "tpl", "sh", "exe", "bin", "ps1", "git",
    "html", "htm", "css",
    "jpg", "jpeg", "png", "gif", "svg", "webp", "ico",
    "woff", "woff2", "ttf", "eot",
    "mp4", "webm", "ogg", "mp3", "wav", "mov",
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"
]

# =============================================================================
# Separa los archivos de las carpetas y los categoriza segun su extencion
# =============================================================================
def add_to_tree(tree, path_parts, all_files):
    current = tree

    for part in path_parts:
        clean_part = part.split("?")[0]

        for ext in exts:
            if clean_part.endswith(f".{ext}"):
                all_files.setdefault(ext, {"Amount": 0, "Files": []})
                all_files[ext]["Amount"] += 1
                all_files[ext]["Files"].append(clean_part)

        if part not in current:
            current[part] = {}
        current = current[part]

    return all_files


# =============================================================================
# Construye el arbol de directorios a partir de la lista de URLs y paths
# =============================================================================
def build_directory_tree(links):
    global all_files

    directory_tree = {}

    for link in links:
        if link.startswith('#'):
            continue

        path_parts = link.strip('/').split('/')
        add_to_tree(directory_tree, path_parts, all_files)

    return directory_tree, all_files