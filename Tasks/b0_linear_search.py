"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
from typing import Any

def search_elem(elem: Any, arr: Any) -> bool:
    '''
    :param elem:
    :param arr:
    :return:
    '''
    for el in arr:
        if el == elem:
            return True
        return False

def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if not arr:
        mn = -1
        mi = -1
    else:
        mn = arr[0]
        mi = 0
    for ind, el in enumerate(arr):
        if el < mn:
            mn = el
            mi = ind
    print(arr)
    return mi
