#!/usr/local/bin/python
import random

from algorithms.bucket_sort import bucket_sort


def main():
    random.seed(0)
    values = []
    for x in range(10000):
        values.append(random.randint(1, 10000))
    bucket_sort(values)


if __name__ == '__main__':
    main()
