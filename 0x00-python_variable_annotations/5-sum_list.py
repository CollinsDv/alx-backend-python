#!/usr/bin/env python3
"""module: 5-sum_list"""
from typing import List
# Write a type-annotated function sum_list which takes a list input_list
# of floats as argument and returns their sum as a float.


def sum_list(input_list: List[float]) -> float:
    """sums an array of floats in a list"""
    sum = 0
    for floatNum in input_list:
        sum += floatNum

    return sum
