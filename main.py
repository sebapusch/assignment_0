"""Add two lists of inst."""

import numpy as np


def add_two_integer_lists(a: list[int], b: list[int]) -> None:
    """Add two lists of integers.

    :param a: first list of ints
    :param b: second list of ints
    """
    arr = np.array(a) + np.array(b)
    print(f"My added array: {arr}")


if __name__ == "__main__":
    add_two_integer_lists([1, 2, 3], [4, 5, 6])
