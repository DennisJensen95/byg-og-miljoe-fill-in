# Standard library
import unittest
import pathlib
import json

# Module to test
from read_pdf_details import locate_all_words_in_save_line_and_order_them, locate_keyword_top, populate_details_data


class TestReadPdfDetails(unittest.TestCase):
    
    def setUp(self):
        with open("../test_artifacts/image_data.json", "r") as f:
            self.data = json.load(f)
        

    def test_locating_words_in_line(self):
        
        words = locate_all_words_in_save_line_and_order_them(self.data, 385.0)
        
        self.assertEqual(words[0], "Grundejer")
        self.assertEqual(words[1], "Marcus Mathiesen")
        
    def test_locate_keyword(self):
        # 1
        # Happy case
        top_value = locate_keyword_top(self.data, "grundejer")
        self.assertEqual(top_value, 385.0)
        
        # 2
        # No detected keyword case
        top_value = locate_keyword_top(self.data, "Grundejer45")
        self.assertEqual(top_value, -1)
    
    def test_read_certificate_details(self):
        details = populate_details_data(self.data)

        # First block data
        self.assertEqual(details["grundejer"], "Marcus Mathiesen")
        self.assertEqual(details["udførelsesadresse"],
                         "Knudensvej 7 9900 Frederikshavn")

        # Second block data
        self.assertEqual(details["rekvirent"], "Marcus Mathiesen")
        self.assertEqual(details["telefon"], "71757709")
        self.assertEqual(details["emailadresse"],
                         "Marcusmullermat@hotmail.com")

        # Third block of data
        self.assertEqual(details["kommune"], "Frederikshavn")
        self.assertEqual(details["matrikel"], "20ø")
        self.assertEqual(details["placering"], "Nedgravet")
        self.assertEqual(details["størrelse"], "4000 liter")
        self.assertEqual(details["fabrikat/type"],
                         "Herning Beholder Fabrik A/S")
        self.assertEqual(details["etableringsår"], "1984")
        self.assertEqual(details["fabrikationsnr"], "324450")
        self.assertEqual(details["typenr"], "01-000")
        self.assertEqual(details["indhold"], "Fyringsolie")

        # Fourth block of data
        self.assertEqual(
            details["opgave udført"], "Tanken er tømt og påfyldningsstuds samt udluftningsrør er afmonteret (afskåret) og afblændet")
        self.assertEqual(details["dato for udførelse"], "14-10-2022")
        self.assertEqual(details["internt sagsnr"], "24441")
        
