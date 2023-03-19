"""Collection of helper functions."""
from typing import Generator

def integer_partition(n: int) -> Generator:
    """Generates integer partitions of a positive integer n.

    Implementation by Jerome Kelleher, see:
    https://jeromekelleher.net/generating-integer-partitions.html
    """

    a = [0 for _ in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

def sorted_integer_partition(n: int) -> list:
    """Returns all integer partitions of a positive integer n.

    Args:
        n (int): A positive integer to partition.
    Returns:
        (list): A list of sorted (descending order) tuples.

    Example:
    sorted_integer_partition(3):
    >>> [(1, 1, 1), (2, 1), (3,)]
    """
    return [tuple(sorted(part, reverse=True)) for part in integer_partition(n)]
