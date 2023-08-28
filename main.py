#!/usr/bin/env python

"""
    - ccwc - Coding Challenge Word Count
    - Recreation of the wc unix command line tool (https://codingchallenges.fyi/challenges/challenge-wc)
    
    main.py
"""

from os import path
import re
from args_setup import args_setup


def main(args):
    """Function deals with the single or multiple argument flags given, and works out which function to call depending on flags input.

    Parameters:
        args: Namespace.

    Returns:
        None.

    Raises:
        None.

    """

    # If -c flag given
    if args.c:
        print(count_bytes(args.c))
    # If -l flag given
    if args.l:
        print(count_lines(args.l))
    # If -w flag given
    if args.w:
        print(count_words(args.w))


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
        return f"   {file_size} {path.basename(file_name)}"
    except FileNotFoundError:
        return f"File: {path.basename(file_name)} not found."
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

        return f"   {total_lines} {path.basename(file_name)}"
    except FileNotFoundError:
        return f"File: {path.basename(file_name)} not found."
    except OSError:
        return "OS error occurred."


def count_words(file_name):
    """Function counts the total number of words in a given file.

    Parameters:
        file_name (str): Path to a file.

    Returns:
        str: The total number of word in a file and file name.

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.

    """
    total_words = 0

    try:
        with open(file_name, "r") as file:
            for line in file:
                words = line.split()
                total_words += len(words)

        return f"   {total_words} {path.basename(file_name)}"
    except FileNotFoundError:
        return f"File: {path.basename(file_name)} not found."
    except OSError:
        return "OS error occurred."


if __name__ == "__main__":
    args = args_setup()
    main(args)
