# Standard library
import argparse
from pathlib import Path

# Application libraries
from read_pdf_details import read_certificate_details


def parsing_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filling in the input file arguments to byg og miljø"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
    )
    parser.add_argument(
        "-i",
        "--input-file",
        help="The input file",
        type=str,
        required=True,
    )
    return parser.parse_args()


def main() -> None:
    args = parsing_arguments()
    
    pdf_file = Path(args.input_file).resolve(strict=True)
    read_certificate_details(pdf_file)


if __name__ == "__main__":
    main()
