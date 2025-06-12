# Wooded 🛠️  

## Descripción  
Esta herramienta desarrollada en Python está diseñada para analizar sitios web extrayendo todos los enlaces href y recursos src incrustados en sus páginas. A partir de esta información, reconstruye de manera estructurada un árbol de directorios que representa la organización y distribución de archivos y carpetas dentro del sitio web. Además, clasifica y agrupa los archivos encontrados según sus extensiones, identificando aquellos que podrían ser críticos o sensibles, como archivos de configuración, scripts de backend o logs.

Este enfoque facilita el reconocimiento y mapeo de la superficie de ataque, permitiendo a los profesionales de ciberseguridad y pentesters obtener una visión clara de la estructura y posibles puntos vulnerables de un sitio web. La herramienta es ideal para automatizar la recopilación de información y preparar análisis posteriores más profundos, ayudando a identificar archivos expuestos o configuraciones inapropiadas que podrían comprometer la seguridad del servidor.

Esta herramienta se centra en **entornos educativos y autorizados**, proporcionando un entorno controlado para evaluar la resistencia frente a amenazas de este tipo. Es ideal para realizar auditorías de seguridad, pruebas de capacitaciones en ciberseguridad.

[!warning]
"Esta herramienta se ha creado con fines educativos y de pruebas en entornos controlados. El uso no autorizado no es responsabilidad del desarrollador"
---
![Captura de pantalla](https://i.ibb.co/wNgXCVQq/a-digital-illustration-of-a-terminal-win-mxk5-Dmh-YTPGMg-WOMew-POFA-Ysirh6-PRXyn-LMLgu-Ii2-DA.jpg)
---
## Funciones actuales/futuras
- **ACTUALES**:  
  - **Reconstrucción del árbol de directorios**   
  - **Catalogación de archivos en: alta, media, baja**  
  - **Vínculo directo (path) a archivos y directorios**  
  - **Muestra de archivos agrupados por tipo de extensión**

- **FUTURAS**:
  - **Descarga de archivos**  
  - **Clonación del árbol de directorios en local**  
  - **Almacenamiento del output en formato .txt**  
  - **Evasión de redirecciones**  
  - **Envío de cabeceras en las solicitudes**
---

## Opciones de uso
![Captura de pantalla](https://i.ibb.co/N6xXLf7z/rassssssss.png)

---

## Instalación y uso
1. **Clonar el repositorio**:
  ```bash
    git clone https://github.com/agoralatam/wooded.git
  ```
3. **Entrar a el directorio**:
  ```bash 
   cd wooded
  ```
4.  **Ejecutar script**:
  ```bash 
   python3 -u example.com
  ```
## Video
https://github.com/user-attachments/assets/5b75be25-8769-41fb-9d37-89f8c59435de

---


