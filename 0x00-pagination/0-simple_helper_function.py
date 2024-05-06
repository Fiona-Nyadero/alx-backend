#!/usr/bin/env python3
'''Module for simple helper function'''


def index_range(page: int, page_size: int) -> tuple:
    '''Function that returns a tuple containing
    a start index and an end index'''

    if page <= 0 or page_size <= 0:
        raise ValueError("Provide a positive integer!")

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)
