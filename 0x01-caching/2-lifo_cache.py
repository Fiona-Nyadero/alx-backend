#!/usr/bin/python3
'''Module creates a LIFO caching algorithm'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFOCache is an inherited class from BaseCaching'''

    def __init__(self):
        '''Initializes the LIFOCache class'''
        super().__init__()

    def put(self, key, item):
        '''Assigns item value to key in dictionary'''
        if key is None or item is None:
            return
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                all_keys = list(self.cache_data.keys())
                discarded = all_keys[-1]
                self.cache_data.pop(discarded)
                print("DISCARDED: {}".format(discarded))
            self.cache_data[key] = item

    def get(self, key):
        '''Retrieves the value of key'''
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
