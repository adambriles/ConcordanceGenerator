# /!usr/bin/env python3

import argparse
from argparse import ArgumentParser
from typing import Optional, List

from generate_concordance import ConcordanceUtils
from generate_concordance.concordance_generator import ConcordanceGenerator

"""Concordance Generator

This script reads in a user provided .txt file containing sentences in English. Then -- depending on user provided
options -- writes the generated concordance to a file or stdout.

This script requires that you use Python version 3.8 and have spaCy installed, as well as the English pipeline for
spaCy -- en_core_web_sm.
"""


def main() -> int:
    arg_parser: ArgumentParser = ArgumentParser(
        description="Creates a concordance from a provided text file then writes the concordance to a user specified "
                    "location or stdout.")

    arg_parser.add_argument("-i",
                            "--inputFile",
                            default=None,
                            dest="input_file",
                            help="Location of a text file -- written in English -- used to generate a concordance.",
                            required=True)
    output_location_group = arg_parser.add_mutually_exclusive_group(required=True)
    output_location_group.add_argument("-o",
                                       "--outputFile",
                                       default=None,
                                       dest="output_file",
                                       help="Location the generated concordance text file will be written to.")
    output_location_group.add_argument("-s",
                                       "--stdout",
                                       action="store_true",
                                       default=False,
                                       dest="use_stdout",
                                       help="Print the generated concordance to Stdout.")

    options: argparse.Namespace = arg_parser.parse_args()

    ret_val: int = 1

    # To capture which file could not be accessed as needed, let the get_input_file_text() and write_lines_to_file()
    #   functions try and access the input/output files and report exactly what was wrong with them to the user.
    input_text: Optional[str] = ConcordanceUtils.get_input_file_text(options.input_file)
    if input_text:
        generator = ConcordanceGenerator()
        generator.generate_concordance(text=input_text)

        lines: List[str] = generator.get_concordance_lines()
        if options.use_stdout:
            ConcordanceUtils.print_lines(lines=lines)
            ret_val = 0
        else:
            if ConcordanceUtils.write_lines_to_file(output_file=options.output_file, lines=lines):
                ret_val = 0

    return ret_val


if "__main__" == __name__:
    exit(main())
