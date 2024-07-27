#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Function returns a dict with key value pairs'''
        assert isinstance(index, int)
        assert 0 <= index < len(self.__indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0

        next_idx = index
        data_info = []

        for f in range(index, index + page_size):
            if f in self.__indexed_dataset:
                data_info.append(self.__indexed_dataset[f])
                next_idx = f

        return {
                "index": index,
                "next_idx": next_idx + 1,
                "page_size": page_size,
                "data": data_info,
        }
