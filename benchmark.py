#!/usr/local/bin/python
import random

from algorithms.selection_sort import selection_sort


def main():
    random.seed(0)
    values = []
    for x in range(10000):
        values.append(random.randint(1, 10000))
    selection_sort(values)


if __name__ == '__main__':
    main()
