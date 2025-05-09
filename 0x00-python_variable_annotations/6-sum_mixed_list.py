#!/usr/bin/env python3
"""
Task 6
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats as argument
    and returns their sum as a float.
    """

    return float(sum(mxd_lst))
