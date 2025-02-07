import os
import qrcode
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.utils import ImageReader
import pandas as pd

# Ruta de la fuente Inter-Bold (ajústala si es necesario)
font_path = "Inter/static/Inter_28pt-ExtraBold.ttf"

# Verificar si la fuente existe antes de registrar
if not os.path.exists(font_path):
    raise FileNotFoundError(f"No se encontró la fuente en {font_path}. Verifica la ruta o mueve el archivo a la ubicación correcta.")

# Registrar la fuente en ReportLab
pdfmetrics.registerFont(TTFont("Inter-Bold", font_path))

def create_labels(csv_file, output_pdf):
    """
    Genera un PDF con etiquetas a partir de un archivo CSV.
    Cada línea del CSV genera una página con un rectángulo, texto centrado y un código QR.
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
    c.setFont("Inter-Bold", 60)

    # Dimensiones de la página
    width, height = landscape(letter)

    for label in labels:
        # Configurar la fuente y tamaño de fuente
        c.setFont("Inter-Bold", 60)

        # Dibujar un rectángulo con borde grueso y esquinas redondeadas
        c.setLineWidth(8)  # Grosor del borde
        rect_x = 50
        rect_y = 200
        rect_width = width - 100
        rect_height = height - 400
        c.roundRect(rect_x, rect_y, rect_width, rect_height, 20)  # Esquinas redondeadas con radio 20

        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(label)
        qr.make(fit=True)
        qr_img = qr.make_image(fill='black', back_color='white')
        qr_img_path = f"qr_{label}.png"
        qr_img.save(qr_img_path)

        # Calcular dimensiones del QR
        qr_size = 100  # Tamaño del QR
        qr_x = rect_x + rect_width - qr_size - 20  # Espacio desde el borde derecho del rectángulo
        qr_y = rect_y + (rect_height - qr_size) / 2  # Centrado verticalmente

        # Calcular ancho del texto para centrarlo horizontalmente
        text_width = c.stringWidth(label, "Inter-Bold", 60)
        x_position = rect_x + (rect_width - text_width - qr_size - 20) / 2  # Ajustar para incluir el QR
        y_position = rect_y + (rect_height - 60) / 2  # Centrado verticalmente

        # Dibujar el texto centrado
        c.drawString(x_position, y_position, label)

        # Dibujar el código QR
        c.drawImage(ImageReader(qr_img_path), qr_x, qr_y, width=qr_size, height=qr_size)

        # Crear una nueva página
        c.showPage()

        # Eliminar la imagen QR temporal
        os.remove(qr_img_path)

    # Guardar el PDF
    c.save()
    print(f"PDF '{output_pdf}' generado con éxito.")

# Ejecutar el script con los archivos correspondientes
csv_file = "codigos_lista.csv"  # Asegúrate de tener este archivo en la raíz del proyecto
output_pdf = "etiquetas.pdf"
create_labels(csv_file, output_pdf)
