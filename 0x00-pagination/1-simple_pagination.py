#!/usr/bin/env python3
'''Module creates a simple pagination pagei'''
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Function returns a simple paginated page'''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        first, last = self.index_range(page, page_size)
        return self.dataset()[first:last]

    def index_range(self, page: int, page_size: int) -> tuple:
        '''Function returns a tuple containing
        a start index and an end index'''

        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size

        return (start_idx, end_idx)
