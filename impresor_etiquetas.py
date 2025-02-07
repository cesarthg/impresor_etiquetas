import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
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
    df = pd.read_csv(csv_file)

    # Asegurarse de que hay datos
    if df.empty:
        raise ValueError("El archivo CSV está vacío. Agrega datos antes de ejecutar el script.")

    # Obtener la primera columna como lista de etiquetas
    labels = df.iloc[:, 0].astype(str).tolist()

    # Crear el PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    c.setFont("Inter-Bold", 40)

    # Dimensiones de la página
    width, height = letter

    for label in labels:
        # Dibujar un rectángulo para la etiqueta
        c.rect(50, 200, width - 100, height - 400)

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
