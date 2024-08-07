import pytesseract
from PIL import Image
import re

def extract_text_from_image(image_path):
    """Extrae el texto de la imagen usando OCR."""
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def process_text(text):
    """Procesa el texto extraído para encontrar la fecha, el monto y el local."""
    
    
    fecha_match = re.search(r'\d{2}[/-]\d{2}[/-]\d{4}', text)
    
    
    monto_match = re.search(r'\d{1,3}(?:\.\d{3})*(?:,\d{2})', text)
    
    
    local_match = re.search(r'ZARA|JULERIAQUE|FARMACITY', text, re.IGNORECASE)
    
    fecha = fecha_match.group(0) if fecha_match else 'Fecha no encontrada'
    monto = monto_match.group(0).replace(".", "").replace(",", ".") if monto_match else 'Monto no encontrado'
    local = local_match.group(0) if local_match else 'Local no encontrado'

    return fecha, monto, local

def compare_data(extracted_data, user_data):
    """Compara los datos extraídos con los datos ingresados por el usuario."""
    return extracted_data == user_data


image_path = 'facturas.jpg'
extracted_text = extract_text_from_image(image_path)
print("Texto extraído: ", extracted_text)


extracted_data = process_text(extracted_text)
print("Datos extraídos: ", extracted_data)


user_data = {
    'fecha': '07/08/2024',  
    'monto': '79980.00',    
    'local': 'ZARA'         
}


if compare_data(extracted_data, user_data):
    print("Factura aprobada automáticamente")
else:
    print("Discrepancia encontrada, se requiere revisión manual")
