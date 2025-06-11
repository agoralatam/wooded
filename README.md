# Wooded 🛠️  

## Descripción  
Esta herramienta desarrollada en Python está diseñada para analizar sitios web extrayendo todos los enlaces href y recursos src incrustados en sus páginas. A partir de esta información, reconstruye de manera estructurada un árbol de directorios que representa la organización y distribución de archivos y carpetas dentro del sitio web. Además, clasifica y agrupa los archivos encontrados según sus extensiones, identificando aquellos que podrían ser críticos o sensibles, como archivos de configuración, scripts de backend o logs.

Este enfoque facilita el reconocimiento y mapeo de la superficie de ataque, permitiendo a los profesionales de ciberseguridad y pentesters obtener una visión clara de la estructura y posibles puntos vulnerables de un sitio web. La herramienta es ideal para automatizar la recopilación de información y preparar análisis posteriores más profundos, ayudando a identificar archivos expuestos o configuraciones inapropiadas que podrían comprometer la seguridad del servidor.

Esta herramienta se centra en **entornos educativos y autorizados**, proporcionando un entorno controlado para evaluar la resistencia frente a amenazas de este tipo. Es ideal para realizar auditorías de seguridad, pruebas de capacitaciones en ciberseguridad.

---
![Captura de pantalla](https://i.ibb.co/wNgXCVQq/a-digital-illustration-of-a-terminal-win-mxk5-Dmh-YTPGMg-WOMew-POFA-Ysirh6-PRXyn-LMLgu-Ii2-DA.jpg)
---
## Características Principales  
- **Protocolos Soportados**:  
  - **TCP**   
  - **UDP**
  - **ICMP**

- **Tipos de Ataques**:
  - **ICMP Land Attack**
  - **SYN Land Attack**
  - **TCP Land Attack**
  - **UDP Land Attack**
  - **SYN Flood Attack**
  - **ICMP Smurf Attack**
  - **TCP Smurf Attack**
  - **UDP Smurf Attack**
  - **Ping Death Attack** 
---

## Requisitos del Sistema  
- **Sistema Operativo**: Linux  
- **Permisos:** Root
---

## Instalación y uso
1. **Clonar el repositorio**:
  ```bash
    git clone https://github.com/tu_usuario/barrette.git
  ```
3. **Entrar a el directorio**:
  ```bash 
   cd barrette
  ```
4.  **Otorgar permisos**:
  ```bash 
   chmod 777 * && chmod 777 modules_attack/*
  ```
5. **Instalación de dependencias:**
  ```bash 
   bash install.sh
  ```
