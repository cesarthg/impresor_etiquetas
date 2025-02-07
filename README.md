# Impresor Etiquetas

## Descripción
**Impresor Etiquetas** es un generador de etiquetas en formato PDF a partir de un archivo CSV. Utiliza la fuente **Inter** y permite crear hojas individuales con textos personalizados. Es ideal para la organización de productos, almacenamiento o cualquier uso que requiera etiquetas impresas de manera automatizada.

## Características
- Genera un archivo PDF con una página por cada etiqueta.
- Usa la fuente **Inter** para un diseño moderno y legible.
- Permite personalización de tamaño y alineación del texto.
- Compatible con macOS y sistemas Linux.

## Requisitos
- Python 3.x
- Librerías necesarias: `pandas`, `reportlab`
- Fuente **Inter** descargada y ubicada en el directorio del proyecto.

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/cesarthg/ImpresorEtiquetas.git
   cd ImpresorEtiquetas
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En macOS/Linux
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Descargar la fuente **Inter** y guardarla en la carpeta del proyecto.

## Uso
1. Colocar un archivo `datos.csv` con una columna conteniendo los textos de las etiquetas.
2. Ejecutar el script para generar el PDF:
   ```bash
   python generar_etiquetas.py
   ```
3. El archivo `etiquetas.pdf` se generará en la misma carpeta del proyecto.

## Estructura del Proyecto
```
ImpresorEtiquetas/
│── venv/                 # Entorno virtual (ignorado en Git)
│── datos.csv             # Archivo CSV con los textos de etiquetas
│── Inter-Bold.ttf        # Fuente Inter (descargar y colocar aquí)
│── generar_etiquetas.py  # Script principal
│── requirements.txt      # Dependencias
│── README.md             # Documentación
│── etiquetas.pdf         # Archivo generado
```

## Contribución
Si deseas contribuir, puedes hacer un fork del repositorio y enviar un pull request con mejoras o nuevas funcionalidades.

## Licencia
Este proyecto está bajo la licencia MIT, lo que significa que puedes usarlo y modificarlo libremente.

---
**Autor:** César HG
