def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    elif n < 1:
        return 0
    elif n < 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

    print(n)
    return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    result = 0
    if n < 0:
        raise ValueError
    elif n < 1:
        result = 0
    elif n < 2:
        result = 1
    else:
        cnt = 1
        prev = [0, 1]
        while cnt < n:
            cnt += 1
            result = prev[0] + prev[1]
            prev.append(result)
            prev.pop(0)

    print(f"{str(n)} = {str(result)}")
    return result
