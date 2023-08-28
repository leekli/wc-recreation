#!/usr/bin/env python

"""
    - ccwc - Coding Challenge Word Count
    - Recreation of the wc unix command line tool (https://codingchallenges.fyi/challenges/challenge-wc)
    
    main.py
"""

from os import path
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
        print(f"    {count_bytes(args.c)} {path.basename(args.c)}")
    # If -l flag given
    elif args.l:
        print(f"    {count_lines(args.l)} {path.basename(args.l)}")
    # If -w flag given
    elif args.w:
        print(f"    {count_words(args.w)} {path.basename(args.w)}")
    # If -m flag given
    elif args.m:
        print(f"    {count_characters(args.m)} {path.basename(args.m)}")
    # If not flag given, and only a file name
    else:
        file = args.input_file
        print(
            f"    {count_lines(file)}   {count_words(file)}   {count_bytes(file)} {path.basename(file)}"
        )


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
        return file_size
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

        return total_lines
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

        return total_words
    except FileNotFoundError:
        return f"File: {path.basename(file_name)} not found."
    except OSError:
        return "OS error occurred."


def count_characters(file_name):
    """Function counts the total number of characters in a given file.

    Parameters:
        file_name (str): Path to a file.

    Returns:
        str: The total number of characters in a file and file name.

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.
    """
    total_characters = 0

    try:
        with open(file_name, "r") as file:
            for line in file:
                total_characters += len(line.encode("utf-8"))

        return total_characters
    except FileNotFoundError:
        return f"File: {path.basename(file_name)} not found."
    except OSError:
        return "OS error occurred."


if __name__ == "__main__":
    args = args_setup()
    main(args)
