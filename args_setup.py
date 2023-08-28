"""
    - ccwc - Coding Challenge Word Count
    - Recreation of the wc unix command line tool (https://codingchallenges.fyi/challenges/challenge-wc)
    
    args_setup.py
"""

import argparse
import sys


def args_setup():
    """Function sets up the arguments this app will take using argparse, adds argument help for users, flags available: -c, -l, -w, -m, also takes 1 positional argument if no flags given.

    Parameters:
        None.

    Returns:
        args: Namespace.

    Raises:
        None.
    """

    parser = argparse.ArgumentParser(
        description="ccwc (coding challenge word count) - word, line, character, and byte count"
    )

    # Flag argument for -c
    parser.add_argument(
        "-c",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of bytes in each input file is written to the standard output.",
    )

    # Flag argument for -l
    parser.add_argument(
        "-l",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of lines in each input file is written to the standard output.",
    )

    # Flag argument for -w
    parser.add_argument(
        "-w",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of words in each input file is written to the standard output.",
    )

    # Flag argument for -m
    parser.add_argument(
        "-m",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="The number of characters in each input file is written to the standard output.",
    )

    # Positional, default argument if no flag given
    parser.add_argument(
        "input_file",
        nargs="?",
        help="A positional argument which can take a file name or standard input when no flag is given.",
    )

    args = parser.parse_args()

    return args
