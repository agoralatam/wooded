# Modulos nativos
import argparse
import time
import sys
from colorama import Fore as F, init

# Módulos propios
from banner.banner import banner
from funcs.get_paths import get_url
from funcs.separate_type_paths import parse_links
from funcs.create_directory_tree import build_directory_tree
from funcs.show_data import show_path, show_tree

init(autoreset=True)

ext_critical = [
    "php", "asp", "aspx", "jsp", "cgi", "pl", "py", "rb",
    "sh", "exe", "bin", "ps1",
    "pem", "key", "crt", "p12", "pfx",
    "env", "config", "ini", "yml", "yaml",
    "htaccess", "htpasswd",
    "git",
    "inc", "tpl",
    "log", "sql", "db",
    "bak", "old", "zip", "rar"
]

ext_medium = [
    "js", "json", "xml",
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"
]

ext_low = [
    "html", "htm", "css",
    "jpg", "jpeg", "png", "gif", "svg", "webp", "ico",
    "woff", "woff2", "ttf", "eot",
    "mp4", "webm", "ogg", "mp3", "wav", "mov"
]

# -----------| Argumentos
parser = argparse.ArgumentParser(description="Website file scanner")

parser.add_argument("-u", "--url", required=True, help="Insert a URL")
parser.add_argument("-t", "--tree", action="store_true", help="Show directory tree")
parser.add_argument("-f", "--file-details", action="store_true", help="Show file details")
parser.add_argument("-g", "--get-url-file", action="store_true", help="Show full URLs for files")

args = parser.parse_args()

banner()
links = get_url(args.url)
absolute, relative = parse_links(links)
_, all_files_amount = build_directory_tree(relative)

print(f"\n{F.WHITE}[{F.RED}!{F.WHITE}] {F.WHITE}TARGET{F.RED}> {F.WHITE}{args.url}")
print(f"\n{F.WHITE}╔═══════════════════════════════════════╗")
print(f"{F.WHITE}║               File Found              ║")
print(f"{F.WHITE}╚═══════════════════════════════════════╝\n")
time.sleep(1)

for key, value in all_files_amount.items():
    for i in range(1, value["Amount"] + 1):
        if key in ext_critical:
            category = "critical"
            color = F.RED
        elif key in ext_medium:
            category = "medium"
            color = F.YELLOW
        elif key in ext_low:
            category = "low"
            color = F.GREEN
        else:
            category = "unknown"
            color = F.WHITE

        print(f"\r{F.WHITE}[+] {color}File found {str(key).upper():<8}{F.WHITE}|{color}{i:<5}{F.WHITE}|{color}{category:<10}{F.WHITE}|", end="")
        time.sleep(0.05)

    if value["Amount"] > 0:
        print()


# =============================================================================
# Mostrar detalles de cada archivo
# =============================================================================
if args.file_details:
    print(f"\n\n{F.WHITE}╔═══════════════════════════════════════╗")
    print(f"{F.WHITE}║              File Details             ║")
    print(f"{F.WHITE}╚═══════════════════════════════════════╝\n")
    time.sleep(1)

    for ext, data in all_files_amount.items():
        print(f"[+] {F.YELLOW}FILE TYPE: {ext}")
        for key2, val2 in data.items():
            if key2 == "Amount":
                print(f"    {F.GREEN}{key2}: {val2}")
            else:
                print(f"    {F.GREEN}{key2}:")
                for item in val2:
                    print(f"        {F.RED}• {item}")
        print()


# =============================================================================
# Mostrar arbol de directorios
# =============================================================================
if args.tree:
    print(f"\n{F.WHITE}╔═══════════════════════════════════════╗")
    print(f"{F.WHITE}║             Directory Tree            ║")
    print(f"{F.WHITE}╚═══════════════════════════════════════╝\n")
    time.sleep(1)

    directory_tree, _ = build_directory_tree(relative)
    show_tree(directory_tree)


# =============================================================================
# Mostrar ubicacion de los archivos y directorios
# =============================================================================
if args.get_url_file:
    print(f"\n{F.WHITE}╔═══════════════════════════════════════╗")
    print(f"{F.WHITE}║       URLs Files and Directories      ║")
    print(f"{F.WHITE}╚═══════════════════════════════════════╝\n")

    all_url_file = show_path(relative, args.url)
    for url in all_url_file:
        print(f"[+] {F.GREEN}{url}")

