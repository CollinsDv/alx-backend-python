#!/usr/bin/env python3
"""module: 9-element_length"""
# Annotate the below function’s parameters
# and return values with the appropriate types:
#   def element_length(lst):
#       return [(i, len(i)) for i in lst]
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing a sequence from the input list and its length.

    Args:
        lst (List[Sequence]): A list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
