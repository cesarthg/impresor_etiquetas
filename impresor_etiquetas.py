import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
import pandas as pd

# Ruta de la fuente Inter-Bold (ajústala si es necesario)
font_path = "Inter/static/Inter_28pt-Bold.ttf"

# Verificar si la fuente existe antes de registrar
if not os.path.exists(font_path):
    raise FileNotFoundError(f"No se encontró la fuente en {font_path}. Verifica la ruta o mueve el archivo a la ubicación correcta.")

# Registrar la fuente en ReportLab
pdfmetrics.registerFont(TTFont("Inter-Bold", font_path))

def create_labels(csv_file, output_pdf):
    """
    Genera un PDF con etiquetas a partir de un archivo CSV.
    Cada línea del CSV genera una página con un rectángulo y el texto centrado.
    """
    # Cargar datos del CSV
    df = pd.read_csv(csv_file, dtype=str)  # Leer datos como strings para preservar ceros iniciales

    # Asegurarse de que hay datos
    if df.empty:
        raise ValueError("El archivo CSV está vacío. Agrega datos antes de ejecutar el script.")

    # Obtener la primera columna como lista de etiquetas
    labels = df.iloc[:, 0].tolist()

    # Crear el PDF en orientación horizontal
    c = canvas.Canvas(output_pdf, pagesize=landscape(letter))
    c.setFont("Inter-Bold", 40)

    # Dimensiones de la página
    width, height = landscape(letter)

    for label in labels:
        # Configurar la fuente y tamaño de fuente
        c.setFont("Inter-Bold", 40)

        # Dibujar un rectángulo con borde grueso y esquinas redondeadas
        c.setLineWidth(3)  # Grosor del borde
        c.roundRect(50, 200, width - 100, height - 400, 20)  # Esquinas redondeadas con radio 20

        # Calcular ancho del texto para centrarlo
        text_width = c.stringWidth(label, "Inter-Bold", 40)
        x_position = (width - text_width) / 2
        y_position = height / 2

        # Dibujar el texto centrado
        c.drawString(x_position, y_position, label)

        # Crear una nueva página
        c.showPage()

    # Guardar el PDF
    c.save()
    print(f"PDF '{output_pdf}' generado con éxito.")

# Ejecutar el script con los archivos correspondientes
csv_file = "codigos_lista.csv"  # Asegúrate de tener este archivo en la raíz del proyecto
output_pdf = "etiquetas.pdf"
create_labels(csv_file, output_pdf)
