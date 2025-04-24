#!/usr/bin/env python3
""" Task 9"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annnotated version """
    return [(i, len(i)) for i in lst]
