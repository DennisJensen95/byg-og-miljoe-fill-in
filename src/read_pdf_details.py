# Standard imports
from cmath import log
from pathlib import Path
import tempfile

# Third party libraries
from pdf2image import convert_from_path
import requests
from logger import getLogger


_data_expected = ["grundejer",
                  "udførelsesadresse",
                  "rekvirent",
                  "telefon",
                  "emailadresse",
                  "kommune",
                  "matrikel",
                  "placering",
                  "størrelse",
                  "fabrikat/type",
                  "etableringsår",
                  "fabrikationsnr",
                  "typenr",
                  "indhold",
                  "opgave udført",
                  "dato for udførelse",
                  "internt sagsnr",
                  "noter"]

pixels_range_top = 20

module_log = getLogger(__file__)


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

def locate_all_words_in_save_line_and_order_them(data: dict, top: int) -> dict:
    """Locates the attribute and value in the data"""
    
    words = []

    lines = data["ParsedResults"][0]["TextOverlay"]["Lines"]
    for line in lines: 
        first_word_position_top = line["Words"][0]["Top"]
        if top_equals_range(first_word_position_top, top, pixels_range_top):
            words.append(line["LineText"].strip(".").strip(":"))
    
    return words

def top_equals_range(top: int, top_match: int, range_top: int) -> bool:
    """Checks if the top value is within the range"""
    return top_match - range_top <= top <= top_match + range_top

def locate_keyword_top(data: dict, keyword: str) -> int:
    
    lines = data["ParsedResults"][0]["TextOverlay"]["Lines"]
    
    for line in lines: 
        if keyword in line["LineText"].lower():
            return line["Words"][0]["Top"]
    
    return -1

def populate_details_data(data: dict) -> dict:
    """Populates the details data from the pdf file"""

    details = {}
    
    for keyword in _data_expected:
        top_value = locate_keyword_top(data, keyword)
        words = locate_all_words_in_save_line_and_order_them(data, top_value)
        if len(words) < 2:
            module_log.warning(f"Not able to populate all required fields. Missing: {keyword}")
        details[keyword] = " ".join(words[1:])
    return details
    

def read_certificate_details(path_to_pdf_file: Path, api_key: str) -> dict:
    """Reads the details from the pdf file"""

    image_files = convert_pdf_file_to_image(path_to_pdf_file)
    
    payload = {'isOverlayRequired': True,
               'apikey': api_key,
               'language': "dan",
               }
    
    image_file_descriptor = open(image_files[0], 'rb')
    
    r = requests.post('https://api.ocr.space/parse/image',
                          files={"image": image_file_descriptor},
                          data=payload,
                          )
    
    details = populate_details_data(r.json())
    
    return details
    
    
    
    
