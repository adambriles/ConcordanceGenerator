import errno
from typing import List, Optional


def get_input_file_text(input_file: str) -> Optional[str]:
    """Reads text from a file.

    Parameters
    ----------
    input_file : str
        File to read text from.

    Returns
    -------
    Optional[str]
        Returns text from the file if the file could be read, otherwise None is returned.
    """

    file_text: Optional[str] = None
    try:
        with open(input_file, "r") as file:
            input_file_lines = list()
            for line in file:
                input_file_lines.append(line)
        file_text = "".join(input_file_lines)
    except IOError as io_error:
        if errno.ENOENT == io_error.errno:
            print(f"The provided input file -- {input_file} -- does not exist.")
        elif errno.EACCES == io_error.errno:
            print(f"The provided input file -- {input_file} -- cannot be read.")
        else:
            print(f"An unknown IO error occurred while attempting to read the provided input file -- {input_file}.")
        return file_text

    return "".join(input_file_lines)


def print_lines(lines: List[str]):
    """Prints lines to stdout.

    Lines should not end with a newline character, otherwise two newlines will be printed for every line.

    Parameters
    ----------
    lines : str
        Lines to write to stdout.
    """
    for line in lines:
        print(line)


def write_lines_to_file(lines: List[str], output_file: str) -> bool:
    """Writes lines to output file.

    Each line printed has a newline added to the end.

    Parameters
    ----------
    lines : str
        Lines to be written to output_file.
    output_file : str
        File to write lines to.

    Returns
    -------
    bool
        Returns True if lines were written to file.
    """

    success: bool = False
    try:
        with open(output_file, "w") as file:
            for line in lines:
                file.write(f"{line}\n")
        success = True
    except IOError as io_error:
        if errno.EACCES == io_error.errno:
            print(f"The provided output file -- {output_file} -- cannot be opened for writing.")
        elif errno.EISDIR == io_error.errno:
            print(f"The provided output file -- {output_file} -- is a directory.")
        else:
            print(f"An unknown IO error occurred while attempting to open the provided output "
                  f"file -- {output_file} -- for writing.")

    return success
