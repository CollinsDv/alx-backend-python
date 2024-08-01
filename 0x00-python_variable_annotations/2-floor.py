#!/usr/bin/env python3
"""module: 2-floor
"""
# Write a type-annotated function floor which takes
# a float n as argument and returns the floor of the float.
import math


def floor(n: float) -> int:
    """floors an float value"""
    return math.floor(n)
