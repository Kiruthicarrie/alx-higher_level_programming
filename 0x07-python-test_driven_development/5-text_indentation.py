#!/usr/bin/python3
"""Contains definition of text_indentation() function"""


def text_indentation(text):
    """Print given text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): Text to be formatted.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ss = 0
    for i, j in enumerate(text):
        if j in '.?:':
            print(text[ss: i + 1].strip() + '\n')
            ss = i + 1
    if ss < len(text):
        print(text[ss:].strip(), end="")
