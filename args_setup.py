"""
    - ccwc - Coding Challenge Word Count
    - Recreation of the wc unix command line tool (https://codingchallenges.fyi/challenges/challenge-wc)
    
    args_setup.py
"""

import argparse


def args_setup():
    """Function sets up the arguments this app will take using argparse, adds argument help for users, flags available: -c, -l, -w, -m

    Parameters:
        None.

    Returns:
        args: Namespace.

    Raises:
        None.
    """

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

    parser.add_argument(
        "-w",
        type=str,
        help="The number of words in each input file is written to the standard output.",
    )

    parser.add_argument(
        "-m",
        type=str,
        help="The number of characters in each input file is written to the standard output.  If the current locale does not support multibyte characters, this is equivalent to the -c option.  This will cancel out any prior usage of the -c option.",
    )

    args = parser.parse_args()

    return args
