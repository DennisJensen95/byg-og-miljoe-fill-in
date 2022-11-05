# Standard library
import argparse
from pathlib import Path
import json

# Application libraries
from read_pdf_details import read_certificate_details, populate_details_data
from logger import getLogger
from fill_out_form import FillOutForm

logger = getLogger(__file__)


def parsing_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filling in the input file arguments to byg og miljø"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=['CRITICAL', 'FATAL', 'ERROR', 'WARN', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'],
        help="Set log level",
    )
    parser.add_argument(
        "-i",
        "--input-file",
        help="The input file",
        type=str,
        required=True,
    )
    
    parser.add_argument("--api-key", help="The api key", type=str, required=True)
    return parser.parse_args()


def main() -> None:
    args = parsing_arguments()
    
    logger.setLevel(args.log_level)
    
    pdf_file = Path(args.input_file).resolve(strict=True)
    
    # read_certificate_details(pdf_file, args.api_key)
    
    with open("./test_artifacts/image_data.json", "r") as f:
        data = json.load(f)
    details = populate_details_data(data)
    
    fillOutForm = FillOutForm(details)
    fillOutForm.fill_out_form()
    

if __name__ == "__main__":
    main()
