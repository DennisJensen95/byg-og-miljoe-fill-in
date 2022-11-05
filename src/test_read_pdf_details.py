# Standard library
import unittest
import pathlib

# Module to test
from read_pdf_details import readCertificateDetails


class TestReadPdfDetails(unittest.TestCase):
    def test_read_certificate_details(self):
        file = pathlib.Path("../test_artifacts/24441.pdf")
        details = readCertificateDetails(file)

        # First block data
        self.assertEqual(details["landOwner"], "Marcus Mathiesen")
        self.assertEqual(details["executionAdress"],
                         "Knudensvej 7 9900 Frederikshavn")

        # Second block data
        self.assertEqual(details["requester"], "Marcus Mathiesen")
        self.assertEqaul(details["phone"], "71757709")
        self.assertEqual(details["email"],
                         "Marcusmullermat@hotmail.com")

        # Third block of data
        self.assertEqual(details["commune"], "Frederikshavn")
        self.assertEqual(details["cadastre"], "20ø")
        self.assertEqual(details["placement"], "Nedgravet")
        self.assertEqual(details["size"], "4000 liter")
        self.assertEqual(details["brand"],
                         "Herning Beholder Fabrig A/S")
        self.assertEqual(details["establishmentYear"], "1984")
        self.assertEqual(details["fabricationNumber"], "324450")
        self.assertEqual(details["typeNumber"], "01-000")
        self.assertEqual(details["contents"], "Fyringsolie")

        # Fourth block of data
        self.assertEqual(
            details["executionDescription"], "Tanken er tømt og påfyldningsstuds samt udluftningsrør er afmonteret (afskåret) og afblændet")
        self.assertEqual(details["executionDate"], "14-10-2022")
        self.assertEqual(details["caseNumber"], "24441")
