#!/usr/local/bin/python
import random

from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort


def main():
    random.seed(0)
    values = []
    for x in range(10000):
        values.append(random.randint(1, 10000))


if __name__ == '__main__':
    main()
