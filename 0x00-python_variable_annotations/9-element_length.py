#!/usr/bin/env python3
"""module: 9-element_length"""
from typing import List, Tuple
# Annotate the below function’s parameters
# and return values with the appropriate types:
#   def element_length(lst):
#       return [(i, len(i)) for i in lst]


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """returns a tuple from list operation
    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, where each tuple
                               contains a string and its length.
    """
    return [(i, len(i)) for i in lst]
