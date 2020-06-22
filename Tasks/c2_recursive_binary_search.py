from typing import Sequence, Optional

'''
рекурсивный поиск в b1
'''


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if not arr:
        return None
    elif len(arr) == 1:
        return None if arr[0] != elem else 0

    left = 0
    right = len(arr)

    print("elem " + str(elem))

    while left != right:
        mid = (right - left) // 2 + left
        # print(f"{left} < {mid} < {right}")
        # print("-------")
        if elem > arr[mid]:
            # print("@")
            left = mid+1
        elif elem < arr[mid]:
            right = mid
        else:
            break

    while mid != 0 and elem == arr[mid-1]:
        mid -= 1

    print(elem, arr)
    return None if arr[mid] != elem else mid
