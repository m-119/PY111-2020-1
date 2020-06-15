from typing import Sequence, Optional

#обычный бинарный поиск не учитывает просмотр вправо (для поиска первого элемента)
def subsearch(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    middle = len(arr) // 2  # середина

    if middle == 0:  # если элемент один
        if arr[0] == elem:  #
            return 0
        else:
            return None
    else:
        if elem < arr[middle]:  # искомое - слева
            bs = subsearch(elem, arr[:middle])
            if bs is not None:  # поиск в блоке слева
                return bs
        else:  # искомое - справа
            bs = subsearch(elem, arr[middle:])
            if bs is not None:  # поиск в блоке справа
                return bs + middle
    return None

#вариант 2, не учитывает поиск влево
def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    ind = subsearch(elem, arr) # бинарный поиск

    if ind is None:
        return ind

    for indx in range(ind, 0, -1):
        if arr[ind] == arr[indx]:
            ind = indx
        else:
            break
    return ind
