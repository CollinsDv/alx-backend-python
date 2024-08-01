#!/usr/bin/env python3
"""module: 6-sum_mixed_list
"""
from typing import List, Union
# Write a type-annotated function sum_mixed_list which takes a list mxd_lst of
# integers and floats and returns their sum as a float.


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """sums a list and returns result as a float"""
    return float(sum(mxd_lst))
