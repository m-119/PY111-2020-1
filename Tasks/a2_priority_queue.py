"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

COUNT_PRIORITY = 11
priority_deque = {p: [] for p in range(COUNT_PRIORITY)}

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param priority:
    :param elem: element to be added
    :return: Nothing
    """
    global priority_deque
    priority_deque[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global priority_deque
    for j in range(COUNT_PRIORITY):
        if priority_deque[j]:
            return priority_deque[j].pop(0)
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param priority:
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global priority_deque
    if priority_deque.get(priority, False):
        if ind < len(priority_deque.get(priority)):
            return priority_deque.get(priority)[ind]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_deque
    priority_deque = {p: [] for p in range(COUNT_PRIORITY)}
    return None
