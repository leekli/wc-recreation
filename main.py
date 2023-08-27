#!/usr/bin/env python

"""
    - ccwc - Coding Challenge Word Count
    - Recreation of the wc unix command line tool (https://codingchallenges.fyi/challenges/challenge-wc)
    
    main.py
"""

from os import path
import argparse


def main():
    # Command line arguments setup
    parser = argparse.ArgumentParser(
        description="ccwc - word, line, character, and byte count"
    )
    parser.add_argument(
        "-c",
        type=str,
        help="The number of bytes in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-l",
        type=str,
        help="The number of lines in each input file is written to the standard output.",
    )

    args = parser.parse_args()

    print(args)

    # If -c flag given
    if args.c:
        print(count_bytes(args.c))
    # If -l flag given
    if args.l:
        print(count_lines(args.l))


def count_bytes(file_name):
    """Function counts the total bytes of a given file.

    Parameters:
        file_name (str): Path to a file.

    Returns:
        str: The total file size in bytes and file name.

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.

    """
    try:
        file_size = path.getsize(file_name)
        return f"{file_size} {path.basename(file_name)}"
    except FileNotFoundError:
        return "File not found."
    except OSError:
        return "OS error occurred."


def count_lines(file_name):
    """Function counts the total lines of a given file.

    Parameters:
        file_name (str): Path to a file.

    Returns:
        str: The total number of lines in a file and file name.

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.

    """
    total_lines = 0

    try:
        with open(file_name, "r") as file:
            for line in file:
                total_lines += 1

        return f"{total_lines} {path.basename(file_name)}"
    except FileNotFoundError:
        return "File not found."
    except OSError:
        return "OS error occurred."


if __name__ == "__main__":
    main()
