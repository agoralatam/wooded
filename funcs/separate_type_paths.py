# =============================================================================
# Recibe una lista de enlaces y paths. Luego los serapa en grupos de 'ruta absoluta' y 'ruta relativa'
# =============================================================================
def parse_links(links):
    absolute_path = []
    relative_path = []

    for link in links:
        if not link:
            continue
        
        if link.startswith('http') or link.startswith('www.') or link.endswith('.com'):
            try:
                base_url = link.split('/')[2]
            except:
                pass
            path = '/'.join(link.split('/')[3:])
            relative_path.append(path)
            absolute_path.append(link)

        else:
            relative_path.append(link)

    return absolute_path, relative_path

