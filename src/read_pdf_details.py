# Standard imports
from importlib.resources import path
from pathlib import Path
import tempfile

# Third party libraries
from pdf2image import convert_from_path
from PIL import Image
import pytesseract


def convert_pdf_file_to_image(path_to_pdf_file: Path):
    """Converts the pdf file to an image"""
    
    images = convert_from_path(path_to_pdf_file)
    image_files = []
    for i in range(len(images)):
        # Save pages as images in the pdf
        img_path_file = Path(tempfile.gettempdir()).joinpath(f"page{i}.jpg")
        
        images[i].save(img_path_file, 'JPEG')
        image_files.append(img_path_file)
        
    return image_files

def read_certificate_details(path_to_pdf_file: Path) -> dict:
    """Reads the details from the pdf file"""

    image_files = convert_pdf_file_to_image(path_to_pdf_file)
    
    pdf_text = ""
    
    for image in image_files:
        file = Image.open(image)
        pdf_text.join(pytesseract.image_to_string(file, lang='eng'), "\n")
    
    
    
