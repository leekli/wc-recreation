#!/usr/bin/env python

"""
    - ccwc - Coding Challenge Word Count
    - Recreation of the wc unix command line tool (https://codingchallenges.fyi/challenges/challenge-wc)
    
    ccwc.py
"""

from os import path, remove
from args_setup import args_setup
import sys
from random import randint


def main(args):
    """Function deals with the either no or single argument flags given, and works out which function to call depending on flags input, or a default positional argument if no flags given. Takes in standard input (stdin) if no value (filename) given.

    Parameters:
        args: Namespace.

    Returns:
        None.

    Raises:
        None.
    """

    # If -c flag given
    if args.c:
        if args.c.name != "<stdin>":
            print(f"    {count_bytes(args.c.name)} {path.basename(args.c.name)}")
        else:
            print(f"    {count_bytes(args.c)}")
    # If -l flag given
    elif args.l:
        if args.l.name != "<stdin>":
            print(f"    {count_lines(args.l.name)} {path.basename(args.l.name)}")
        else:
            print(f"    {count_lines(args.l)}")
    # If -w flag given
    elif args.w:
        if args.w.name != "<stdin>":
            print(f"    {count_words(args.w.name)} {path.basename(args.w.name)}")
        else:
            print(f"    {count_words(args.w)}")
    # If -m flag given
    elif args.m:
        if args.m.name != "<stdin>":
            print(f"    {count_characters(args.m.name)} {path.basename(args.m.name)}")
        else:
            print(f"    {count_characters(args.m)}")
    else:
        # If no flag arguments are given, but a file name is
        if args.input_file is not None:
            file = args.input_file
            print(
                f"    {count_lines(file)}   {count_words(file)}   {count_bytes(file)} {path.basename(file)}"
            )
        # If no flag arguments given, but standard input (stdin) is and no file name
        else:
            stdin_content = sys.stdin.read()
            file_name = f"{randint(2452, 387628)}.txt"

            # Create temporary file to store stdin data
            with open(file_name, "w") as file:
                file.write(stdin_content)

            print(
                f"    {count_lines(file_name)}   {count_words(file_name)}   {count_bytes(file_name)}"
            )

            # Delete temporary file if print successful
            if path.exists(file_name):
                remove(file_name)


def count_bytes(file_name):
    """Function counts the total bytes of a given file or standard input (stdin).

    Parameters:
        file_name (str): Path to a file or standard input (stdin).

    Returns:
        str: The total size in bytes of file or standard input (stdin).

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.
    """
    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode("utf-8")

            bytes_size = len(bytes(stdin_content))

            return bytes_size
        else:
            try:
                file_size = path.getsize(file_name)
                return file_size
            except FileNotFoundError:
                return f"File: {path.basename(file_name)} not found."
    except OSError:
        return "OS error occurred."


def count_lines(file_name):
    """Function counts the total lines of a given file or standard input (stdin).

    Parameters:
        file_name (str): Path to a file or standard input (stdin).

    Returns:
        str: The total number of lines in a file or standard input (stdin).

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.
    """
    total_lines = 0

    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode("utf-8")

            lines = stdin_content.splitlines()

            for line in lines:
                total_lines += 1

            return total_lines
        else:
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
    """Function counts the total number of words in a given file or standard input (stdin).

    Parameters:
        file_name (str): Path to a file or standard input (stdin).

    Returns:
        str: The total number of words in a file or standard input (stdin).

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.
    """
    total_words = 0

    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode("utf-8")

            words = stdin_content.split()
            total_words += len(words)

            return total_words
        else:
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
    """Function counts the total number of characters in a given file or standard input (stdin).

    Parameters:
        file_name (str): Path to a file or standard input (stdin).

    Returns:
        str: The total number of characters in a file or standard input (stdin).

    Raises:
        FileNotFoundError: If file name is invalid.
        OSError: If any other error occurs.
    """
    total_characters = 0

    try:
        if file_name is sys.stdin:
            stdin_content = sys.stdin.read().encode("utf-8")

            for char in stdin_content:
                total_characters += 1

            return total_characters
        else:
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
